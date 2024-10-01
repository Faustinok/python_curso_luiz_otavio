import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# criar tabela 
'''cursor.execute(
    f' create table clientes'
    '('
    'id integer primary key autoincrement,'
    'nome text'
    ')'
)
connection.commit() '''
sql = 'insert into clientes (nome) values (?)'
# insert
cursor.execute(
    'insert into clientes (nome) values ("gabriel")'
)
connection.commit()
# insert many 
cursor.executemany( sql,[['gabriel'], ['joao'], ['pedro']])

connection.commit()

# SQL CLOSE
cursor.close()
connection.close()