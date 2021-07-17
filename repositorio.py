import mysql.connector

def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database= 'CADASTRO',
        user= 'root',
        password='Gui281209'
    )
    return db


def insert(db, nome, sobrenome, cpf, email, telefone):
    
    comando_sql = "INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES (%s,%s,%s,%s,%s)"
    valores = (nome, sobrenome, cpf, email, telefone)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, valores)
        db.commit()
        cursor.close()
        print(' novo contato inserido !!!')
    except:
        print('Contato não inserido.')