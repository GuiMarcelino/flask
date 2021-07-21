from flask import Flask, render_template, redirect, request, url_for
from db_connection import conexao, insert
from werkzeug.utils import secure_filename
from flask import jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def pagina_inicial():
    return render_template('index.html')


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')

    elif request.method == "POST":
        row = request.files['tabfile'].readlines()
        lines = []
        for index in row(0, len(row), 1):
            index.decode('utf8').replace('\n', '').split('\t')
            lines.append(index)

        return jsonify(lines)


@app.route('/salvar', methods=['GET, POST'])
def salvar():
    id = request.form["id"]
    purchaser_name = request.form["purchaser_name"]
    item_descripion = request.form["item_descripion"]
    item_price = request.form["item_price"]
    merchant_address = request.form["merchant_address"]
    merchant_name = request.form["merchant_name"]
    db = conexao()
    insert(db, id, purchaser_name, item_descripion, item_price, merchant_address, merchant_name)
    return redirect('/upload')


if __name__ == '__main__':
    app.run(debug=True)
