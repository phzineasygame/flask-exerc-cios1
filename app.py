from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():

     return render_template("pagina.html")

@app.route('/versao')
def versao():
    versao = "1.0.0"  
    return f"App v{versao}"

@app.route('/saudar/<nome>')
def saudar(nome):
    nome_capitalizado = nome.capitalize()  
    return f"Olá, {nome_capitalizado}!"
