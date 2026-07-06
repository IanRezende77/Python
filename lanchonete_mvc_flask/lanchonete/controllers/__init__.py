from .home_controller import home_bp
from .cliente_controller import cliente_bp
from .fornecedor_controller import fornecedor_bp


def registrar_blueprints(app):
    """Centraliza o registro dos Blueprints da camada Controller."""
    app.register_blueprint(home_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(fornecedor_bp)
