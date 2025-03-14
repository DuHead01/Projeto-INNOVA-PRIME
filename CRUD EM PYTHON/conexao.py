import sqlite3


# Conexão com o banco de dados
conn = sqlite3.connect('innovaPrime.db')

# Criação do cursor
cursor = conn.cursor()

# Criação da tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS cliente ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'sobrenome' TEXT, 'correspondente' TEXT, 'processoTipo' TEXT, 'data' TEXT)""")


