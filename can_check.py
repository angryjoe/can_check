#!/Users/jstelmach/bs4/bin/python

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('http://treehousebrew.com/on-tap')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull text from all instances of <a> tag within BodyText div
strong = soup.find_all('strong', limit=5)

for thing in strong:
    updated = thing.contents[0]
    if "UPDATED" in updated:
        print(updated)

available_cans = soup.find('div', {'id':'block-yui_3_17_2_3_1431874277695_22362'})
cans = available_cans.find_all('a')


for can in cans:
    c = can.contents[0]
    print(c)
