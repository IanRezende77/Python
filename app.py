from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # feito
import os

app = Flask(__name__)

# feito
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'loja.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# feito
db = SQLAlchemy(app)


# feito
class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Produto {self.nome}>"


# feito
with app.app_context():
    db.create_all()


# LISTAR
@app.route("/")
def lista_produtos():
    # feito
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template("lista.html", produtos=produtos)


# CADASTRAR
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar_produto():

    if request.method == "POST":

        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()

        try:
            preco = float(request.form.get("preco", 0))
        except:
            preco = 0

        try:
            estoque = int(request.form.get("estoque", 0))
        except:
            estoque = -1

        # feito
        if not nome or not categoria or preco <= 0 or estoque < 0:
            erro = "Preencha os campos corretamente."
            return render_template(
                "formulario.html",
                produto=None,
                erro=erro
            )

        # feito
        produto = Produto(
            nome=nome,
            categoria=categoria,
            preco=preco,
            estoque=estoque
        )

        db.session.add(produto)
        db.session.commit()

        return redirect(url_for("lista_produtos"))

    return render_template("formulario.html", produto=None)


# EDITAR
@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar_produto(produto_id):

    # feito
    produto = Produto.query.get_or_404(produto_id)

    if request.method == "POST":

        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()

        try:
            preco = float(request.form.get("preco", 0))
        except:
            preco = 0

        try:
            estoque = int(request.form.get("estoque", 0))
        except:
            estoque = -1

        # feito
        if not nome or not categoria or preco <= 0 or estoque < 0:
            erro = "Preencha os campos corretamente."
            return render_template(
                "formulario.html",
                produto=produto,
                erro=erro
            )

        # feito
        produto.nome = nome
        produto.categoria = categoria
        produto.preco = preco
        produto.estoque = estoque

        db.session.commit()

        return redirect(url_for("lista_produtos"))

    return render_template("formulario.html", produto=produto)


# EXCLUIR
@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir_produto(produto_id):

    # feito
    produto = Produto.query.get_or_404(produto_id)

    db.session.delete(produto)
    db.session.commit()

    return redirect(url_for("lista_produtos"))


if __name__ == "__main__":
    app.run(debug=True)
