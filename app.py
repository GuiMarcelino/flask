from flask import Flask, render_template, redirect, request



app = Flask(__name__)

@app.route('/', methods =['get'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/cadastro', methods=['get'])
def cadastro():
    return render_template("cadastro.html")

@app.route('/salvar', methods=['post'])
def salvar():
    nome = request.form["first_name","last_name","cpf","email","phone"]
    sobrenome = request.form["last_name"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["phone"]
    return redirect('/cadastro')


app.run(debug=True)


