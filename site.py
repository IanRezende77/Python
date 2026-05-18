from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Página profissional
@app.route("/profissional")
def page1():
    return render_template("page1.html")

# Página expectativas
@app.route("/expectativas")
def page2():
    return render_template("page2.html")

@app.route("/sobre")
def page3():
    return render_template("page3.html")

if __name__ == "__main__":
    app.run(debug=True)