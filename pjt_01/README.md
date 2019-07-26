# API를 이용하여 영화정보 추출하기



## 목표

- 영화 평점서비스(ex : watcha)를 만들기 위한 데이터 수집단계로, 영화 DB구축을 위한 csv 파일을 만든다.



## 과정



1. 영화 진흥원에서 API KEY를 할당받고 해당 KEY를 이용하여 API에 접근한다.

   

2. 최근 50주간 데이터 중에 주간 박스오피스 TOP 10 데이터를 수집한다.

    - 주간(월~일)까지 기간의 데이터를 조회한다.

    - 조회 기간은 총 50주 이며, 기준일(마지막 일자)은 2019년 7월 13일로 한다.

      

3.  requests모듈을 import하여 해당 URL을 만들어 정보에 대한 요청을 보낸다.

   | 코드    | 내용     | 코드    | 내용     | 코드    | 내용       |
   | ------- | -------- | ------- | -------- | ------- | ---------- |
   | movieCd | 영화코드 | movieNm | 영화이름 | AudiAcc | 누적관객수 |

   - API상세에서 각 정보로의 접근 코드를 확인한 후 이를 사용하여 정보들을 수집한다.
   - 수집 대상은 영화 대표코드, 영화명(국문), 영화명(영문) , 영화명(원문) , 관람등급 , 개봉연도 , 상영시간 , 장르 , 감독명이고 영화인 항목에서 감독의 상세정보도 추출한다.



## 방법



1. 추출한 내용을 decouple, csv 모듈을  import해서 파일로 작성해준다.

   - ```python
     from decouple import config
     
     key = config('API_KEY')
     ```

     decouple모듈에 있는 import 함수를 이용하여 API_KEY를 .env에서 가져올 수 있다.

   - .gitignore에  . env를 기입하여 github에 올릴 때 commit되지 않게한다.

2. Requests모듈을 import하여 API에 정보를 요청하고 받아온다.

   - ```python
     import requests
     base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
     targetDt = datetime(2019, 7, 13) - timedelta(weeks = weeks_ago)
     targetDt = targetDt.strftime('%Y%m%d')
     api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0'
     response = requests.get(api_url)
     data = response.json()['boxOfficeResult']['weeklyBoxOfficeList']
     ```

   - API상세에 맞춰 api_url에 원하는 것을 요청할 수 있는 url을 만들어서 넣고 이를 requests.get()을 이용하여 요청하고 결과값을 반환받는다.



3. Csv모듈을 import하여 csv파일을 읽고 작성한다.

   - ```python
     import csv
     with open('../pjt_01/movies.csv', 'r', newline='', encoding='utf-8') as f:
         reader = csv.DictReader(f)
     ```

     open의 2번째 position 값을 'r'로 해서 만들어놓은 csv파일을 읽어들이고 사용할 수 있다.

   - ```python
     with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
         fieldnames = ('movieCd', 'link', 'image', 'userRating')
         writer = csv.DictWriter(f, fieldnames=fieldnames)
         writer.writeheader()
         for i in all_movie.values():
             writer.writerow(i)
     ```

     open의 2번째 position 값을 'w'로 해서 csv파일을 작성할 수 있다.

