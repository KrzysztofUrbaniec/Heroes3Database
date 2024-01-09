import functools
import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def create_mysql_connection(func):
    '''Create a connection to MySQL server. 
    
    It's a wrapper function, which allows to modulate the behavior of other functions interacting with databases.

    Args:
        func: function, upon which the wrapper is intended to act.
    '''

    @functools.wraps(func)
    def wrapper(host,user,password,database=None,*args,**kwargs):
        with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        ) as connection:
            func(connection,*args,**kwargs)

    return wrapper

@create_mysql_connection
def create_table(connection: mysql.connector.connection_cext.CMySQLConnection, table_query: str) -> None:
    '''Create table in an existing database.
    
    Args:
        connection: mysql.connector's object representing a connection to a database.
        table_query: query responsible for table creation.
    '''
    with connection.cursor() as cursor:
        try:
            cursor.execute(table_query)
        except mysql.connector.Error as err:
            print(err.msg)
    print('Table created.')

@create_mysql_connection
def insert_into_table(connection: mysql.connector.connection_cext.CMySQLConnection, table_name: str, data: list) -> None:
    '''Insert data into an existing table.
    
    Args:
        connection: mysql.connector's object representing a connection to a database.
        table_name: name of the table to insert data into.
        data: a list of dictionaries containing data to insert into the table.
    '''
    with connection.cursor() as cursor:
        insert_query = generate_insert_query(data,table_name)        
        cursor.executemany(insert_query, data)
        connection.commit()

def generate_insert_query(data: list, table_name: str) -> str:
    '''Dynamically generate an insertion query using "data" dictionary.'''

    if not isinstance(data,list):
        raise TypeError('data must be a list')
    if not isinstance(table_name, str):
        raise TypeError('table_name must be a string')
    if len(data) == 0:
        raise ValueError('data cannot be an empty container')
    if all([isinstance(x,dict) for x in data]) is not True:
        raise ValueError('some of the elements of data are not dictionaries')
    if len({len(x.keys()) for x in data}) > 1:
        raise ValueError('some of the dictionaries inside data have various number of keys')
        
    first_keys = set(data[0].keys())
    key_comparison = all(set(d.keys()) == first_keys for d in data[1:])
    if key_comparison is not True:
        raise ValueError('some dictionaries inside data have various key names')

    columns_list = ', '.join(data[0].keys())
    values_list = ', '.join(list(map(lambda x: '%(' + str(x) + ')s',data[0].keys())))
    insert_query = f"INSERT INTO {table_name} ({columns_list}) VALUES ({values_list})"
    return insert_query