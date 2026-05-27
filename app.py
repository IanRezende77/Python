from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        resultado, erro = calcular(request.form)

    return render_template("calculadora.html", resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)