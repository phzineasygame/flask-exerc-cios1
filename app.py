from flask import Flask, render_template, redirect, url_for

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

@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}"

@app.route('/home')
def redirecionar_home():
    return redirect(url_for('home'))

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

def buscar(item):
    itens = ["banana", "maçã", "laranja", "uva"]  
    encontrado = False  

    
    for i in itens:
        if i == item:
            encontrado = True
            break

    if encontrado:
        return f"Item '{item}' encontrado!"
    else:
        return f"Item '{item}' não encontrado."

if __name__ == '__main__':
    app.run(debug=True)






