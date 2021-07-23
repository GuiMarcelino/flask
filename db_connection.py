import mysql.connector


def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database='VELOW',
        user='root',
        password='Gui281209'
    )
    return db


def insert(db, purchaser_name, item_description, item_price, purchase_count, merchant_address, merchant_name):
    comando_sql = "INSERT INTO VENDAS (PURCHASER_NAME, ITEM_DESCRIPTION, ITEM_PRICE, PURCHASE_COUNT, MERCHANT_ADDRESS, MERCHANT_NAME) VALUES (%s,%s,%s,%s,%s,%s)"
    valores = (purchaser_name, item_description, item_price, purchase_count, merchant_address, merchant_name)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, valores)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)


def calc(db):
    cursor = db.cursor()
    cursor.execute("SELECT SUM(ITEM_PRICE*PURCHASE_COUNT) FROM VENDAS")
    resultado_calc = cursor.fetchall()
    print(resultado_calc)
    cursor.close()
    return f'Valor total Bruto:{resultado_calc}'
