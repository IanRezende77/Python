from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import db
from models.fornecedor import Fornecedor

fornecedor_bp = Blueprint("fornecedor", __name__, url_prefix="/fornecedores")


@fornecedor_bp.route("/", methods=["GET", "POST"])
def listar_fornecedores():
    if request.method == "POST":
        nome_empresa = request.form.get("nome_empresa", "").strip()
        cnpj = request.form.get("cnpj", "").strip()
        produto_fornecido = request.form.get("produto_fornecido", "").strip()

        if not nome_empresa or not cnpj or not produto_fornecido:
            flash("Empresa, CNPJ e produto fornecido sao obrigatorios.", "erro")
            return redirect(url_for("fornecedor.listar_fornecedores"))

        try:
            novo_fornecedor = Fornecedor(
                nome_empresa=nome_empresa,
                cnpj=cnpj,
                produto_fornecido=produto_fornecido,
            )
            db.session.add(novo_fornecedor)
            db.session.commit()
            flash("Fornecedor cadastrado com sucesso.", "sucesso")
        except Exception:
            db.session.rollback()
            flash("Nao foi possivel cadastrar o fornecedor.", "erro")

        return redirect(url_for("fornecedor.listar_fornecedores"))

    fornecedores = Fornecedor.query.order_by(Fornecedor.data_criacao.desc()).all()
    return render_template("fornecedores.html", fornecedores=fornecedores)
