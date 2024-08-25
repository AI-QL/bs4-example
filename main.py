# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def extract_magnets(url):
    response = requests.get(url)
    response.raise_for_status()  # Check successful

    soup = BeautifulSoup(response.text, 'html.parser')

    hrefs = [a['href'] for a in soup.find_all(href=True)]

    magnets = [href for href in hrefs if href.startswith('magnet:')]

    return magnets

if __name__ == "__main__":
    url = 'https://annas-archive.org/torrents/duxiu'  # Replace to your URL
    magnets = extract_magnets(url)
    for magnet in magnets:
        print(magnet)
