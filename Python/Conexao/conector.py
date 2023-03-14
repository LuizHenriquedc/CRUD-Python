import mysql.connector

try:
    conn = mysql.connector.connect(user='teste', password='',
                                   host='127.0.0.1',
                                   database='pessoas')
    print("Conectado")

except:
    print("Erro de conexão")