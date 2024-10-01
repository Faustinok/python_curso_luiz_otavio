import pymysql
import dotenv
import os
dotenv.load_dotenv()
connection = pymysql.connect(
    host= os.environ['BD_HOST'],
    user=os.environ['BD_USER'],
    password=os.environ['BD_PASSWORD'],
    database= os.environ['BD_DATABASE']
)
with connection:
    with connection.cursor() as cursor:
            cursor.execute(
                f' create table clientes'
                '('
                'id int not null auto_increment,'
                'nome text,'
                'idade int not null'
                ')'
            )
            connection.commit()
    with connection.cursor() as cursor:
            cursor.execute(
                f' insert into clientes'
                '('
                'nome,idade,'
                ')'
                'values("gabriel",12)'
            )
            connection.commit()        