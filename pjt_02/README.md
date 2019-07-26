# API를 이용하여 영화정보 추출하기



## 목표

- 영화 평점서비스(ex : watcha)를 만들기 위한 데이터 수집이후 영화의 평점 및 하이퍼 텍스트 링크, 이미지 링크를 추출하고 이미지 링크를 이용하여 이미지 파일을 작성한다.



## 과정



1. Naver Developers에서 API의 Client_id와 Client_pw를 받아오고 URL 요청정보를 기입하여 정보를 받아온다.

   

2. 지난 프로젝트에서 추출한 csv 파일에서 영화 이름을 읽어와서 Naver 영화 검색 API에 자료를 요청한다.

   - 영화별로 영진위 영화 대표코드 , 하이퍼텍스트 link , 영화 썸네일 이미지의 URL , 유저 평점을 저장한다

     

3.  이미지 URL을 통해 해당 image를 요청하고 csv모듈을 통해 image파일을 만들어 준다

   - 수



## 방법



1. 추출한 내용을 decouple, csv 모듈을  import해서 파일로 작성해준다.

   - ```python
     from decouple import config
     
     CLIENT_ID = config('CLIENT_ID')
     CLIENT_SECRET = config('CLIENT_SECRET')
     ```

     decouple모듈에 있는 import 함수를 이용하여 client_id와 client_secret을 .env에서 가져올 수 있다.

   - .gitignore에  . env를 기입하여 github에 올릴 때 commit되지 않게한다.

     

2. Requests모듈을 import하여 API에 정보를 요청하고 받아온다.

   - ```python
     import requests
     
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
     with open(f'images/{Cd}.jpg', 'wb') as f:
         response = requests.get(i['image'])
         f.write(response.content)
     ```

     open의 2번째 position 값을 'wb'로 해서 이미지파일을 작성할 수 있다.