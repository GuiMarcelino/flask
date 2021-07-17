from flask import Flask, render_template, redirect, request
from repositorio import conexao, insert


app = Flask(__name__)

@app.route('/', methods =['get'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/cadastro', methods=['get'])
def cadastro():
    return render_template("cadastro.html")

@app.route('/salvar', methods=['post'])
def salvar():
    nome = request.form["first_name"]
    sobrenome = request.form["last_name"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["phone"]
    db = conexao()
    insert(db, nome , sobrenome, cpf, email, telefone)
    return redirect('/cadastro')


app.run(debug=True)


