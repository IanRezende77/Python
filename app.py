from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nome = "Carlos"
    idade = 16

    usuario = {
        "nome": "Carlos",
        "email": "carlos@email.com"
    }

    alunos = ["João", "Maria", "Pedro"]

    nota = 8


    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        usuario=usuario,
        alunos=alunos,
        nota=nota
    )

if __name__ == "__main__":
    app.run(debug=True)