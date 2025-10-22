from flask import Flask, render_template, request, redirect, url_for, flash, abort, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from urllib.parse import urlparse
import logging
import json
from werkzeug.middleware.proxy_fix import ProxyFix
import sys

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuração do proxy
app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_port=1,
    x_prefix=1
)

# Configurações básicas
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave_secreta_123')
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Headers de segurança
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self' https: 'unsafe-inline' 'unsafe-eval' data:;"
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response
db = SQLAlchemy(app)

# Modelos
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    daily_tasks = db.relationship('DailyTask', backref='category', lazy=True)

class DailyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='pendente')
    priority = db.Column(db.String(10), default='media')
    area = db.Column(db.String(100), nullable=True)
    scheduled_date = db.Column(db.Date, nullable=False)
    scheduled_time = db.Column(db.String(5), nullable=True)
    duration_hours = db.Column(db.Float, default=1.0, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def get_task_statistics():
    try:
        total_tasks = DailyTask.query.count()
        completed_tasks = DailyTask.query.filter_by(status='concluida').count()
        pending_tasks = DailyTask.query.filter_by(status='pendente').count()
        in_progress = DailyTask.query.filter_by(status='em_andamento').count()
        
        # Calculate completion rate
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        # Tasks by priority
        high_priority = DailyTask.query.filter_by(priority='alta').count()
        medium_priority = DailyTask.query.filter_by(priority='media').count()
        low_priority = DailyTask.query.filter_by(priority='baixa').count()
        
        # Tasks by category
        category_stats = db.session.query(
            Category.name,
            db.func.count(DailyTask.id)
        ).join(DailyTask, isouter=True).group_by(Category.name).all()
        
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'in_progress': in_progress,
            'completion_rate': round(completion_rate, 2),
            'priority_stats': {
                'high': high_priority,
                'medium': medium_priority,
                'low': low_priority
            },
            'category_stats': dict(category_stats) if category_stats else {}
        }
    except Exception as e:
        print(f"Error getting statistics: {e}")
        return {
            'total_tasks': 0,
            'completed_tasks': 0,
            'pending_tasks': 0,
            'in_progress': 0,
            'completion_rate': 0,
            'priority_stats': {
                'high': 0,
                'medium': 0,
                'low': 0
            },
            'category_stats': {}
        }

@app.route('/')
def index():
    tasks = DailyTask.query.filter_by(status='pendente').order_by(DailyTask.scheduled_date, DailyTask.scheduled_time).all()
    categories = Category.query.all()
    stats = get_task_statistics()
    
    # Get upcoming deadlines
    upcoming_deadlines = DailyTask.query.filter_by(status='pendente')\
        .filter(DailyTask.scheduled_date >= datetime.now().date())\
        .order_by(DailyTask.scheduled_date)\
        .limit(5).all()
    
    return render_template('index.html',
                         tasks=tasks,
                         categories=categories,
                         stats=stats,
                         upcoming_deadlines=upcoming_deadlines)

@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    try:
        if request.method == 'POST':
            # Validação dos campos obrigatórios
            required_fields = ['title', 'scheduled_date', 'category_id', 'priority']
            for field in required_fields:
                if field not in request.form or not request.form[field]:
                    flash(f'O campo {field} é obrigatório!', 'error')
                    return redirect(url_for('new_task'))

            try:
                scheduled_date = datetime.strptime(request.form['scheduled_date'], '%Y-%m-%d').date()
            except ValueError:
                flash('Data inválida!', 'error')
                return redirect(url_for('new_task'))

            task = DailyTask(
                title=request.form['title'],
                description=request.form.get('description', ''),
                category_id=request.form['category_id'],
                area=request.form.get('area', ''),
                scheduled_date=scheduled_date,
                scheduled_time=request.form.get('scheduled_time', ''),
                duration_hours=float(request.form.get('duration_hours', 1.0)),
                priority=request.form['priority']
            )
            db.session.add(task)
            db.session.commit()
            flash('Tarefa criada com sucesso!', 'success')
            return redirect(url_for('index'))

        categories = Category.query.all()
        if not categories:
            flash('É necessário criar categorias antes de adicionar tarefas!', 'warning')
        return render_template('new_task.html', categories=categories)
    except Exception as e:
        logger.error(f'Erro ao criar tarefa: {str(e)}')
        db.session.rollback()
        flash('Erro ao criar tarefa. Por favor, tente novamente.', 'error')
        return redirect(url_for('new_task'))

@app.route('/task/<int:task_id>/complete')
def complete_task(task_id):
    task = DailyTask.query.get_or_404(task_id)
    task.status = 'concluida'
    task.completed_at = datetime.utcnow()
    db.session.commit()
    flash('Tarefa concluída!')
    return redirect(url_for('index'))

def init_db():
    try:
        with app.app_context():
            # Criar o banco de dados
            db.create_all()
            
            # Verificar se já existem categorias
            if Category.query.first() is None:
                # Criar categorias iniciais
                categories = [
                    Category(name='Saúde', description='Atividades relacionadas à saúde e bem-estar'),
                    Category(name='Casa', description='Tarefas domésticas'),
                    Category(name='Trabalho', description='Atividades profissionais'),
                    Category(name='Estudo', description='Atividades educacionais'),
                    Category(name='Lazer', description='Atividades de entretenimento')
                ]
                for category in categories:
                    db.session.add(category)
                db.session.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.session.rollback()

# Inicializa o banco de dados quando o app é criado
@app.before_first_request
def create_tables():
    try:
        db.create_all()
        # Verificar se já existem categorias
        if Category.query.first() is None:
            # Criar categorias iniciais
            categories = [
                Category(name='Saúde', description='Atividades relacionadas à saúde e bem-estar'),
                Category(name='Casa', description='Tarefas domésticas'),
                Category(name='Trabalho', description='Atividades profissionais'),
                Category(name='Estudo', description='Atividades educacionais'),
                Category(name='Lazer', description='Atividades de entretenimento')
            ]
            for category in categories:
                db.session.add(category)
            db.session.commit()
            logger.info("Banco de dados inicializado com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao inicializar banco de dados: {e}")
        db.session.rollback()

# Healthcheck route
@app.route('/healthcheck')
def healthcheck():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return Response(
            response=json.dumps({'status': 'healthy', 'database': 'connected'}),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        logger.error(f'Healthcheck failed: {e}')
        return Response(
            response=json.dumps({'status': 'unhealthy', 'error': str(e)}),
            status=500,
            mimetype='application/json'
        )

# Debug route
@app.route('/debug')
def debug():
    if not app.debug:
        return Response(
            response=json.dumps({'message': 'Debug mode is disabled'}),
            status=403,
            mimetype='application/json'
        )
    
    debug_info = {
        'request_headers': dict(request.headers),
        'environment': dict(os.environ),
        'database_uri': app.config['SQLALCHEMY_DATABASE_URI'],
        'config': {k: str(v) for k, v in app.config.items() if k not in ['SECRET_KEY']}
    }
    return Response(
        response=json.dumps(debug_info, indent=2),
        status=200,
        mimetype='application/json'
    )

# Error handlers
@app.errorhandler(400)
def bad_request_error(error):
    logger.error(f'Bad request: {error}')
    if request.is_json:
        return jsonify({'error': 'Bad Request', 'message': str(error)}), 400
    return render_template('error.html', error=error), 400

@app.errorhandler(404)
def not_found_error(error):
    logger.error(f'Page not found: {error}')
    if request.is_json:
        return jsonify({'error': 'Not Found', 'message': str(error)}), 404
    return render_template('error.html', error=error), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Server Error: {error}')
    db.session.rollback()
    if request.is_json:
        return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500
    return render_template('error.html', error=error), 500

@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f'Unhandled exception: {error}', exc_info=True)
    db.session.rollback()
    if request.is_json:
        return jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred'}), 500
    return render_template('error.html', error='An unexpected error occurred'), 500

@app.before_request
def before_request():
    logger.info(f'Incoming request: {request.method} {request.url}')
    if not request.url.startswith('https://') and 'localhost' not in request.url:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)