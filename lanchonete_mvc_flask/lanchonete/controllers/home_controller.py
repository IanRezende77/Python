from flask import Blueprint, render_template
from models.cliente import Cliente
from models.fornecedor import Fornecedor

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def index():
    total_clientes = Cliente.query.count()
    total_fornecedores = Fornecedor.query.count()
    return render_template(
        "index.html",
        total_clientes=total_clientes,
        total_fornecedores=total_fornecedores,
    )
