from flask import Flask

app = Flask(__name__)

@app.route('/decorator')

def explicar_decorator():
    return """
    <h1>Decorators em Python</h1>

    <h2>O que é um decorator?</h2>
    <p>
    Um decorator é uma função que modifica o comportamento de outra função
    sem alterar diretamente seu código.
    </p>

    <h2>Para que serve?</h2>
    <p>
    Serve para reutilizar código, adicionar funcionalidades como validação,
    autenticação, logs, entre outros.
    </p>

    <h2>Como é utilizado no Flask?</h2>
    <p>
    No Flask, usamos decorators para definir rotas.
    Exemplo: <b>@app.route('/decorator')</b>
    </p>

    <p>
    Esse decorator associa a função a uma URL específica.
    </p>
    """
    
if __name__ == '__main__':
    app.run(debug=True)