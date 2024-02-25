import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

f = csv.writer(open('z-artist-names.csv', 'w'))

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())

last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())

for artist_name in artist_name_list_items:
  name= artist_name.contents[0]
  link='https://web.archive.org' + artist_name.get('href')
  f.writerow([name,link])

f = csv.writer(open('z-artist-names.csv', 'w'))

