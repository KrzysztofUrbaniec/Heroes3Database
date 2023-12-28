'''The module contains functions used to scrap data related to different aspects of Heroes of Might and Magic 3.'''

import requests
from bs4 import BeautifulSoup

def fetch_and_parse(URL: str) -> BeautifulSoup:
    '''Fetch and parse page data available at given URL. 
    
    Args:
        URL: URL to requested page.

    Returns: 
        Parsed BeautifulSoup object.'''

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Request Exception: {e}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

def get_creature_data(creature_soup: BeautifulSoup) -> list:
    '''Extract information about different creatures from Heroes 3. 
    
    Args:
        creature_soup: BeautifulSoup object containing scraped html page with creatures table.

    Returns:
        Data prepared for an insertion into MySQL database in format: [(Value1,Value2,...,ValueN),(Value1,Value2,...,ValueN),...] '''

    creatures = []

    table = creature_soup.find_all('tr')[2:]
    for row in table:
        unit_properties = row.find_all('td')
        unit_name = unit_properties[0].text.strip()
        town = unit_properties[1].find('span').get('title').strip()
        level =  unit_properties[2].text.strip()
        attack = unit_properties[3].text.strip()
        defense = unit_properties[4].text.strip()
        min_dmg = unit_properties[5].text.strip()
        max_dmg = unit_properties[6].text.strip()
        health = unit_properties[7].text.strip()
        speed = unit_properties[8].text.strip()
        growth = unit_properties[9].text.strip()
        gold = unit_properties[11].text.strip()
        second_resource = unit_properties[12].text.replace(',','').strip()
        special_abilities = unit_properties[13].text.strip()
            
        if second_resource != '':
            second_resource += ' ' + unit_properties[12].find('a').get('title').strip()

        creatures.append((unit_name, town, level, attack, defense, min_dmg, max_dmg, health, speed, growth, gold, second_resource, special_abilities))

    return creatures

def get_hero_data():
    pass

def get_spell_data():
    pass

def get_artifact_data():
    pass