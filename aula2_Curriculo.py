from flask import Flask

app = Flask(__name__)


@app.route("/Curriculo")
def Curriculo():
    return '''
    <h1>Currículo</h1>

    <h2>Nome</h2>
    <p>Ian Erfurt Rezende</p>

    <h2>Telefone</h2>
    <p>(31) 97116-5285</p>

    <h2>Email</h2>
    <p>ianerfurt@gmil.com</p>

    <h2>Escolas</h2>
    <p>Coleguium 2019-2024, Cotemig 2025-presente</p>

    <h2>Experiências</h2>
    <p>Estagio em TI</p>

    <h2>Cursos</h2>
    <p>Python, HTML, CSS, Javascript, Banco de Dados, PHP,
       C#, Rede e Infraestrutura de computadores.</p>

    <h2>Idiomas</h2>
    <p>Inglês: Intermediário</p>
    '''


if __name__ == "__main__":
    app.run(debug=True)
