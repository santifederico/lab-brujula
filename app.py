from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/metodologia")
def metodologia():
    return render_template("metodologia.html")

@app.route("/plataforma")
def plataforma():
    return render_template("plataforma.html")

@app.route("/observatorio")
def observatorio():
    return render_template("observatorio.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")