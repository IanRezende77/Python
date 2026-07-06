from flask_sqlalchemy import SQLAlchemy

# Instancia unica do banco para toda a aplicacao.
# Ela e inicializada no app.py dentro da factory create_app().
db = SQLAlchemy()
