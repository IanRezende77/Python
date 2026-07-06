from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import db
from models.cliente import Cliente

cliente_bp = Blueprint("cliente", __name__, url_prefix="/clientes")


@cliente_bp.route("/", methods=["GET", "POST"])
def listar_clientes():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        telefone = request.form.get("telefone", "").strip()
        pontos = request.form.get("pontos_fidelidade", "0").strip() or "0"

        if not nome or not telefone:
            flash("Nome e telefone sao obrigatorios para cadastrar um cliente.", "erro")
            return redirect(url_for("cliente.listar_clientes"))

        try:
            pontos_fidelidade = int(pontos)
            novo_cliente = Cliente(
                nome=nome,
                telefone=telefone,
                pontos_fidelidade=pontos_fidelidade,
            )
            db.session.add(novo_cliente)
            db.session.commit()
            flash("Cliente cadastrado com sucesso.", "sucesso")
        except ValueError:
            flash("Os pontos de fidelidade precisam ser um numero inteiro.", "erro")
        except Exception:
            db.session.rollback()
            flash("Nao foi possivel cadastrar o cliente.", "erro")

        return redirect(url_for("cliente.listar_clientes"))

    clientes = Cliente.query.order_by(Cliente.data_criacao.desc()).all()
    return render_template("clientes.html", clientes=clientes)
