import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config

import csv


all_director = {}
with open('movies.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        peopleNm = row['peopleNm']
        movieNm = row['movieNm']
        key = config('API_KEY')  #영화인 코드, 영화인 명, 분야, 필모리스트
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
        api_url = f'{base_url}?key={key}&peopleNm={peopleNm}'

        response = requests.get(api_url)
        data = response.json()
        pp_ls = data['peopleListResult']['peopleList'][0]
        filmo = pp_ls['filmoNames'].split('|')
        if movieNm in filmo:
            if pp_ls['repRoleNm'] == '감독':
                peopleCd = pp_ls['peopleCd']
        set_mo = {
            'peopleCd' : peopleCd,
            'peopleNm' : peopleNm,
            'repRoleNm' : '감독',
            'filmoNames' : ', '.join(filmo),
        }
        all_director.update({peopleCd : set_mo})
with open('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames') 
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for a in all_director.values():
        writer.writerow(a)