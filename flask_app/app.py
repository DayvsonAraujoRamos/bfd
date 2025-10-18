from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
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
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pendente')
    priority = db.Column(db.String(10), default='media')
    scheduled_date = db.Column(db.Date, nullable=False)
    scheduled_time = db.Column(db.String(5))
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    tasks = DailyTask.query.filter_by(status='pendente').order_by(DailyTask.scheduled_date, DailyTask.scheduled_time).all()
    categories = Category.query.all()
    return render_template('index.html', tasks=tasks, categories=categories)

@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        scheduled_date = datetime.strptime(request.form['scheduled_date'], '%Y-%m-%d').date()
        task = DailyTask(
            title=request.form['title'],
            description=request.form['description'],
            category_id=request.form['category_id'],
            scheduled_date=scheduled_date,
            scheduled_time=request.form['scheduled_time'],
            priority=request.form['priority']
        )
        db.session.add(task)
        db.session.commit()
        flash('Tarefa criada com sucesso!')
        return redirect(url_for('index'))
    categories = Category.query.all()
    return render_template('new_task.html', categories=categories)

@app.route('/task/<int:task_id>/complete')
def complete_task(task_id):
    task = DailyTask.query.get_or_404(task_id)
    task.status = 'concluida'
    task.completed_at = datetime.utcnow()
    db.session.commit()
    flash('Tarefa concluída!')
    return redirect(url_for('index'))

def init_db():
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
            db.session.bulk_save_objects(categories)
            db.session.commit()

init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)