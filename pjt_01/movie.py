import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config

import csv
with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    all_movie = {}
    for row in reader:
        print(row)
        movieCd = row['movieCd']

        key = config('API_KEY')
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
        api_url = f'{base_url}?key={key}&movieCd={movieCd}'
        response = requests.get(api_url)
        data = response.json()
        ifs = data['movieInfoResult']['movieInfo']  #영화 하나당 데이터
        genre_no = len(ifs['genres'])
        genres = []
        for i in ifs['genres']:
            genres.append(i['genreNm'])
        if ifs['directors'] == [] :
            director = ''
        else :
            director = ifs['directors'][0]['peopleNm']
        if ifs['audits'] == [] :
            watchGrade = ''
        else :
            watchGrade = ifs['audits'][0]['watchGradeNm']
        genre = ' '.join(genres)
        set_nd = {
            'movieCd':ifs['movieCd'],  #국문, 영문, 원문, 관람등급, 개봉연도, 상연시간, 장르, 감독명
            'movieNm':ifs['movieNm'],
            'movieNmEn':ifs['movieNmEn'],
            'movieNmOg':ifs['movieNmOg'],
            'watchGradeNm' : watchGrade,
            'openDt':ifs['openDt'],
            'showTm':ifs['showTm'],
            'genreNm':genre,
            'peopleNm':director
        }
        all_movie.update({movieCd : set_nd})
        

    import csv
    with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in all_movie.values():
            writer.writerow(i)
