import requests
from bs4 import BeautifulSoup
import json

def getItemsFromPage(url):
    urlResponse = requests.get(url)
    soup = BeautifulSoup(urlResponse.text, 'html.parser')
    itemURLs = []

    rawItems = soup.find('table', {'class': 'ak-table'}).tbody.find_all('tr')

    for item in rawItems:
        item = 'https://www.dofus.com' + item.find('a')['href']
        itemURLs.append(item)
        print(item)

    print(len(itemURLs))

def getItemStats(url):
    urlResponse = requests.get(url)
    soup = BeautifulSoup(urlResponse.text, 'html.parser')

    # get and clean data
    name = soup.find('h1', attrs = {'class': 'ak-return-link'}).text.strip()
    lvl = soup.find('div', attrs = {'class': 'ak-encyclo-detail-level col-xs-6 text-right'}).text[7:0]
    image = soup.find('img', attrs = {'class': 'img-maxresponsive'})["src"]

    rawStats = soup.find('div', {'class': 'ak-container ak-content-list ak-displaymode-col'})
    stats = {}

    for stat in rawStats:
        description = stat.find_next('div', {'class': 'ak-title'}).text.strip()
        type = ""
        maxStat = ""

        if 'to' in description:
            arr = description.split(' ')
            maxStat = arr[2].replace('%', '')
            del arr[0]
            del arr[0]
            del arr[0]
            type = ' '.join(arr)
        else:
            arr = description.split(' ')
            maxStat = arr[0].replace('%', '')
            del arr[0]
            type = ' '.join(arr)

        if '%' in description and "Critical" not in description:
            type = '% ' + type

        stats[type] = {'description': description, 'maxStat': maxStat}

    item = {'name': name, 'lvl': lvl, 'image': image, 'stats': stats}

    return item


getItemsFromPage('https://www.dofus.com/en/mmorpg/encyclopedia/weapons')
