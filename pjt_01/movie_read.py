import csv

fieldnames = ('movieCd', 'movieNm', 'audiAcc')

all_movie = {}

with open('movies.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    

    # 50주간 박스오피스 TOP10 데이터
    for row in reader:
        