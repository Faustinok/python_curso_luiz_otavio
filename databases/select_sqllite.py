import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'select * from clientes')
for row in cursor.fetchall():
    _id ,_nome = row
    print(row[0])
    print(row[1])
    print(f'o id e {_id},  o nome e {_nome}')
cursor.close()
connection.close()