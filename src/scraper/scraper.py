import requests
from bs4 import BeautifulSoup

def fetch_and_parse(URL: str) -> BeautifulSoup:
    '''Fetch and parse page data available at given URL. Returns parsed BeautifulSoup object.'''
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

def get_creature_data():
    pass

def get_hero_data():
    pass

def get_spell_data():
    pass

def get_artifact_data():
    pass