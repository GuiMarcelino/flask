from flask import Flask, render_template, redirect, request, url_for, flash
from db_connection import conexao, insert
from werkzeug.utils import secure_filename
import os
import csv


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'tab'}

def allowed_file(filename):
    # verificação de tipo de arquivo 
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/', methods =['GET'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/upload/', methods=['POST','GET'])
def upload():
        if request.method == "POST":

            if 'tabfile' not in request.files:
                flash('No file part') # flash retorna uma valor de forma rapida 
                return redirect(request.url)
            file = request.files['tabfile']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(f"{app.config['UPLOAD_FOLDER']}/{filename}", 'r') as file: 
                    for line in csv.reader(file,dialect='excel-tab'):
                        print(line)
                return redirect(url_for('upload', name=filename))


        elif request.method == "GET":
            return render_template('upload.html')





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

