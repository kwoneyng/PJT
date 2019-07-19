import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config

all_movie = {}
for w in range(50,0,-1):
    targetDt = datetime(2019, 7, 13) - timedelta(weeks=w)
    targetDt = targetDt.strftime('%Y%m%d')  #strf 특정 포멧으로 바꿔줌

    key = config('API_KEY')
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    api_url = f'{base_url}?key={key}&targetDt={targetDt}'

    response = requests.get(api_url)
    data = response.json()
    movies = data['boxOfficeResult']['weeklyBoxOfficeList']   #코드(5), 영화이름(6), 관객(1) 지금은 영화 뭉탱이
    for movie in movies:
        set_mo = {
            'movieCd' : movie['movieCd'],
            'movieNm' : movie['movieNm'],
            'audiAcc' : movie['audiAcc']
           }
        all_movie.update({movie['movieCd'] : set_mo})
        

    pprint(all_movie)
    print('=================================')


import csv
with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'audiAcc')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in all_movie.values():
        writer.writerow(i)
