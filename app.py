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
    id = request.form["id"]
    purchaser_name = request.form["purchaser_name"]
    item_descripion = request.form["item_descripion"]
    item_price = request.form["item_price"]
    merchant_address = request.form["merchant_address"]
    merchant_name = request.form["merchant_name"]
    db = conexao()
    insert(db, id, purchaser_name , item_descripion, item_price, merchant_address, merchant_name)
    return redirect('/cadastro')


app.run(debug=True)

