import re
from flask import Flask, render_template, redirect, request, url_for, flash
from db_connection import calc, conexao, insert
from werkzeug.utils import secure_filename
import os
import csv

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'tab'}


def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        if 'tabfile' not in request.files:
            flash('No file part')  # flash retorna uma valor de forma rapida
            return redirect(request.url)
        file = request.files['tabfile']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(f"{app.config['UPLOAD_FOLDER']}/{filename}", 'r') as file:

                index = 0

                for line in csv.reader(file, dialect='excel-tab'):
                    if index == 0:
                        index += 1

                    else:
                        salvar(line)

            return redirect(url_for('upload', name=filename))

    elif request.method == "GET":
        return render_template('upload.html')


def salvar(line):
    purchaser_name = line[0]
    item_descripion = line[1]
    item_price = line[2]
    purchaser_count = line[3]
    merchant_address = line[4]
    merchant_name = line[5]
    db = conexao()
    insert(db, purchaser_name, item_descripion, item_price, purchaser_count, merchant_address, merchant_name)

@app.route('/resultado', methods=['GET'])
def result():
    db = conexao()
    resultado = calc(db)
    print(type(resultado))
    return render_template('resultado.html', resultado_no_html=resultado)
    

if __name__ == '__main__':
    app.run(debug=True)
