import os

from dotenv import load_dotenv

load_dotenv()

UNITS_URL = 'https://heroes.thelazy.net/index.php/List_of_creatures'
HEROES_URL = 'https://heroes.thelazy.net/index.php/List_of_heroes'
ARTIFACTS_URL = 'https://heroes.thelazy.net/index.php/List_of_artifacts'

TABLE_CREATION_QUERIES = dict()

TABLE_CREATION_QUERIES['units'] = (
"CREATE TABLE IF NOT EXISTS `units` ("
" `unit_name` VARCHAR(100), `town` VARCHAR(20), `level` VARCHAR(5), `attack` INT, `defense` INT, `min_dmg` INT, `max_dmg` INT, `health` INT, `speed` INT,"
" `growth` INT, `gold` INT, `second_resource` VARCHAR(50), `special_abilities` VARCHAR(255)"
")")

TABLE_CREATION_QUERIES['heroes'] = (
"CREATE TABLE IF NOT EXISTS `heroes` ("
" `hero_name` VARCHAR(20), `class` VARCHAR(20), `specialty` VARCHAR(20), `skill1` VARCHAR(20), `skill2` VARCHAR(20), `spell` VARCHAR(20)"
")")

TABLE_CREATION_QUERIES['artifacts'] = (
"CREATE TABLE IF NOT EXISTS `artifacts` ("
" `artifact_name` VARCHAR(100), `slot` VARCHAR(20), `class` VARCHAR(20), `cost` INT, `effect` VARCHAR(200), `combination` VARCHAR(150)"
")")

DB_PARAMS = {'user': os.getenv('MYSQL_USER'),
             'host': os.getenv('MYSQL_HOST'),
             'password': os.getenv('MYSQL_PASSWORD'),
             'database': 'Heroes3DB'}
