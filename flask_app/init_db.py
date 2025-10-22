from app import db, app
from app import Category

def init_db():
    with app.app_context():
        # Criar todas as tabelas
        db.create_all()
        
        # Verificar se já existem categorias
        if not Category.query.first():
            # Criar categorias iniciais
            categories = [
                Category(name='Saúde', description='Atividades relacionadas à saúde e bem-estar'),
                Category(name='Casa', description='Tarefas domésticas'),
                Category(name='Trabalho', description='Atividades profissionais'),
                Category(name='Estudo', description='Atividades educacionais'),
                Category(name='Lazer', description='Atividades de entretenimento')
            ]
            
            try:
                for category in categories:
                    db.session.add(category)
                db.session.commit()
                print("Categorias iniciais criadas com sucesso!")
            except Exception as e:
                print(f"Erro ao criar categorias: {e}")
                db.session.rollback()
        else:
            print("Categorias já existem no banco de dados.")

if __name__ == '__main__':
    init_db()