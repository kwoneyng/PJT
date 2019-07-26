import requests
from pprint import pprint
from decouple import config
import time

import csv
with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        Cd = i['movieCd']
        with open(f'images/{Cd}.jpg', 'wb') as f:
            response = requests.get(i['image'])
            f.write(response.content)