import requests
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods = ["GET",
    "POST"])
def calcular():
    if  request.method == "POST":
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']
    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1}  + {num2} = {resultado}'
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1}  - {num2} = {resultado}'
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1}  - {num2} = {resultado}'
    elif operacao == '/':
        if num2 != 0:
            resultado = 'Erro'
            etapas = 'Divisão por 0!'
    else:    
        resultado = 'operação invaida'
        etapas = 'A operação selecionada é invalida'
    return render_template('calculadora.html', etapas = etapas, resultados = resultado)

if __name__ == "__main__":
    app.run(debug=True)