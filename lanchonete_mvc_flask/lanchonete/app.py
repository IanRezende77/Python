import os
from flask import Flask
from controllers import registrar_blueprints
from models import db
from models.cliente import Cliente
from models.fornecedor import Fornecedor


def popular_dados_iniciais():
    """Cria alguns dados iniciais apenas quando o banco estiver vazio."""
    if Cliente.query.count() == 0:
        db.session.add_all(
            [
                Cliente(nome="Ana Paula", telefone="(31) 99999-1001", pontos_fidelidade=12),
                Cliente(nome="Carlos Mendes", telefone="(31) 98888-2002", pontos_fidelidade=7),
                Cliente(nome="Juliana Rocha", telefone="(31) 97777-3003", pontos_fidelidade=21),
            ]
        )

    if Fornecedor.query.count() == 0:
        db.session.add_all(
            [
                Fornecedor(
                    nome_empresa="Distribuidora Pao Quente",
                    cnpj="12.345.678/0001-90",
                    produto_fornecido="Paes artesanais",
                ),
                Fornecedor(
                    nome_empresa="Bebidas Minas",
                    cnpj="98.765.432/0001-10",
                    produto_fornecido="Refrigerantes e sucos",
                ),
                Fornecedor(
                    nome_empresa="Hortifruti Central",
                    cnpj="11.222.333/0001-44",
                    produto_fornecido="Verduras e legumes",
                ),
            ]
        )

    db.session.commit()


def create_app(configuracao_teste=None):
    """Application Factory da aplicacao Flask."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="troque-esta-chave-em-producao",
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, "lanchonete.sqlite3"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if configuracao_teste:
        app.config.update(configuracao_teste)

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        popular_dados_iniciais()

    registrar_blueprints(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
