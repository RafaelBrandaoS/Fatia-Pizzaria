from mysql.connector import connect
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USUARIO = os.getenv('DB_USUARIO')
DB_BANCO = os.getenv('DB_BANCO')
DB_PORTA = os.getenv('DB_PORTA')


def criar_conexao():
    return connect(host=DB_HOST, user=DB_USUARIO, password='', database=DB_BANCO, port=DB_PORTA)


def fexar_conexão(con):
    return con.close()
