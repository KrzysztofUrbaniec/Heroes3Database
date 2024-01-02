from src.database import db_manager
from src.scraper import scraper
import src.constants as const

def main():
    # Create tables
    for table in const.TABLE_CREATION_QUERIES.keys():
        print(f'Attempting to create table: {table}')
        db_manager.create_table(const.DB_PARAMS['host'], 
                                const.DB_PARAMS['user'], 
                                const.DB_PARAMS['password'], 
                                const.DB_PARAMS['database'],
                                table_query=const.TABLE_CREATION_QUERIES[table])

    soups = dict()
    data = dict()

    # Scrape the data
    for (name, url) in zip(['units','heroes','artifacts'],[const.UNITS_URL,const.HEROES_URL,const.ARTIFACTS_URL]):
        soups[name] = scraper.fetch_and_parse(url)

    # Extract the data
    data['units'] = scraper.get_creature_data(soups['units'])
    data['heroes'] = scraper.get_hero_data(soups['heroes'])
    data['artifacts'] = scraper.get_artifact_data(soups['artifacts'])

    for table in const.TABLE_CREATION_QUERIES.keys():
        print(f'Attempting to insert data into table: {table}')
        db_manager.insert_into_table(const.DB_PARAMS['host'], 
                                     const.DB_PARAMS['user'], 
                                     const.DB_PARAMS['password'], 
                                     const.DB_PARAMS['database'],
                                     table_name=table,
                                     data=data[table])
        print('Data inserted succesfully.')

if __name__ == '__main__':
    main()