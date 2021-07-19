import mysql.connector

def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database= 'CADASTRO',
        user= 'root',
        password='Gui281209'
    )
    return db


def insert(db, purchaser_name, item_description, item_price, purchase_count, merchant_address, merchant_name):
    
    comando_sql = "INSERT INTO VELOW (PURCHASER_NAME, ITEM_DESCRIPTION, ITEM_PRICE, PURCHASE_COUNT, MERCHANT_ADDRESS, MERCHANT_NAME) VALUES (%s,%s,%s,%s,%s,%s)"
    valores = (purchaser_name, item_description, item_price, purchase_count, merchant_address, merchant_name)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, valores)
        db.commit()
        cursor.close()
        print(' novo contato inserido !!!')
    except:
        print('Contato não inserido.')