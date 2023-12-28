import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def create_mysql_connection(host,user,password,database=None):
    '''Create connection to mysql server.'''

    connection = None
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection

def create_database(connection):
    '''Create a database to store tables with Heroes 3 data'''
    pass

def insert_data(connection,table,data):
    '''Insert data to an existing table.'''
    pass

user = os.getenv('MYSQL_USER')
host = os.getenv('MYSQL_HOST')
password = os.getenv('MYSQL_PASSWORD')

connection = create_mysql_connection(host,user,password)
print(connection)