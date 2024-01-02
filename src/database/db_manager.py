import functools
import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def create_mysql_connection(func):
    '''Create connection to MySQL server.'''

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
def create_table(connection,table_query):
    '''Create table in an existing database.'''
    with connection.cursor() as cursor:
        try:
            cursor.execute(table_query)
        except mysql.connector.Error as err:
            print(err.msg)
    print('Table created.')
        

# Function that performs an SQL insertion operation
@create_mysql_connection
def insert_into_table(connection, table_name, data):
    '''Insert data into an existing table.'''
    with connection.cursor() as cursor:
        columns_list = ', '.join(data[0].keys())
        values_list = ', '.join(list(map(lambda x: '%(' + str(x) + ')s',data[0].keys())))

        insert_query = f"INSERT INTO {table_name} ({columns_list}) VALUES ({values_list})"
        cursor.executemany(insert_query, data)
        connection.commit()

db_params = {'user': os.getenv('MYSQL_USER'),
             'host': os.getenv('MYSQL_HOST'),
             'password': os.getenv('MYSQL_PASSWORD'),
             'database': 'Heroes3DB'}

# Insert data into the table using the decorated function
# insert_into_table(db_params['host'], db_params['user'], db_params['password'], db_params['database'], table, data_to_insert)

from src.scraper import scraper
creature_soup = scraper.fetch_and_parse('https://heroes.thelazy.net/index.php/List_of_creatures')
creature_data = scraper.get_creature_data(creature_soup)

table_query = (
    "CREATE TABLE IF NOT EXISTS `test_table_creatures` ("
    " `unit_name` VARCHAR(100), `town` VARCHAR(20), `level` VARCHAR(5), `attack` INT, `defense` INT, `min_dmg` INT, `max_dmg` INT, `health` INT, `speed` INT,"
    " `growth` INT, `gold` INT, `second_resource` VARCHAR(50), `special_abilities` VARCHAR(255)"
    ")")

create_table(db_params['host'], db_params['user'], db_params['password'], db_params['database'],table_query=table_query)
insert_into_table(db_params['host'], db_params['user'], db_params['password'], db_params['database'],table_name='test_table_creatures',data=creature_data)