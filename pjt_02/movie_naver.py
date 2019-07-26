import requests
from pprint import pprint
from decouple import config
import time

import csv
with open('../pjt_01/movies.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    all_movie = {}

    for row in reader:
        time.sleep(0.1)
        query = row['movieNm']
        BASE_URL='https://openapi.naver.com/v1/search/movie.json'
        CLIENT_ID = config('CLIENT_ID')
        CLIENT_SECRET = config('CLIENT_SECRET')
        HEADERS = {
            'X-Naver-Client-Id' : CLIENT_ID,
            'X-Naver-Client-Secret' : CLIENT_SECRET,
        }
        API_URL = f'{BASE_URL}?query={query}'
        response = requests.get(API_URL, headers=HEADERS).json()
        tar_d = response['items']
        for k in tar_d:
            if k['image'] == '':
                k['image'] = 'None'
            print(k['image'])
            if row['peopleNm'] in k['director']:
                set_nd = {
                    'movieCd':row['movieCd'],
                    'link':k['link'],
                    'image':k['image'],
                    'userRating':k['userRating'],
                }
                all_movie.update({query : set_nd})
with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'link', 'image', 'userRating')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in all_movie.values():
        writer.writerow(i)