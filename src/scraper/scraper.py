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
        Data prepared for an insertion into MySQL database in format: [dict(values),dict(values),...] '''

    creatures = []
    table = creature_soup.find_all('tr')[2:]
    for row in table:
        creature_properties = dict()
        unit_properties = row.find_all('td')
        creature_properties['unit_name'] = unit_properties[0].text.strip()
        creature_properties['town'] = unit_properties[1].find('span').get('title').strip()
        creature_properties['level'] =  unit_properties[2].text.strip()
        creature_properties['attack'] = unit_properties[3].text.strip()
        creature_properties['defense'] = unit_properties[4].text.strip()
        creature_properties['min_dmg'] = unit_properties[5].text.strip()
        creature_properties['max_dmg'] = unit_properties[6].text.strip()
        creature_properties['health'] = unit_properties[7].text.strip()
        creature_properties['speed'] = unit_properties[8].text.strip()
        creature_properties['growth'] = unit_properties[9].text.strip()
        creature_properties['gold'] = unit_properties[11].text.strip()
        creature_properties['second_resource'] = unit_properties[12].text.replace(',','').strip()
        creature_properties['special_abilities'] = unit_properties[13].text.strip()
            
        if creature_properties['second_resource'] != '':
            creature_properties['second_resource'] += ' ' + unit_properties[12].find('a').get('title').strip()

        creatures.append(creature_properties)

    return creatures

def get_hero_data(hero_soup: BeautifulSoup) -> list:
    '''Extract information about different heroes from Heroes 3. 
    
    Args:
        creature_soup: BeautifulSoup object containing scraped html page with heroes table.

    Returns:
        Data prepared for an insertion into MySQL database in format: [dict(values),dict(values),...] '''

    heroes = []
    table = hero_soup.find_all('tr')[2:]
    for row in table:
        hero_properties = dict()
        hero = row.find_all('td')
        hero_properties['hero_name'] = hero[0].text.strip()
        hero_properties['class'] = hero[1].text.strip()
        hero_properties['specialty'] = hero[3].text.strip()
        hero_properties['skill1'] = hero[5].text.strip()
        hero_properties['skill2'] = hero[7].text.strip()
        hero_properties['spell'] = hero[9].text.strip()

        heroes.append(hero_properties)

    return heroes

def get_artifact_data(artifact_soup: BeautifulSoup) -> list:
    '''Extract information about different artifacts from Heroes 3. 
    
    Args:
        creature_soup: BeautifulSoup object containing scraped html page with artifacts table.

    Returns:
        Data prepared for an insertion into MySQL database in format: [dict(values),dict(values),...] '''

    artifacts = []
    table = artifact_soup.find_all('tr')[2:]
    for row in table:
        artifact_properties = dict()
        artifact = row.find_all('td')
        artifact_properties['artifact_name'] = artifact[0].text.strip()
        artifact_properties['slot'] = artifact[1].text.strip()
        artifact_properties['class'] = artifact[2].text.strip()
        artifact_properties['cost'] = artifact[3].text.strip()
        artifact_properties['effect'] = artifact[4].text.strip()
        artifact_properties['combination'] = artifact[5].text.strip()

        artifact.append(artifact_properties)

    return artifacts