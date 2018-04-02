## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## HTTP GET Request
req = requests.get('http://kutis.kyonggi.ac.kr/webkutis/index.jsp')

## HTML 소스 가져오기
html = req.text

# ## HTTP Header 가져오기
# header = req.headers
# ## HTTP Status 가져오기 (200: 정상)
# status = req.status_code
# ## HTTP가 정상적으로 되었는지 (True/False)
# is_ok = req.ok

## BeautifulSoup으로 html소스를 python객체로 변환하기
## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
## 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')
## CSS Selector를 통해 html요소들을 찾아낸다.
my_titles = soup.find_all(
    ["link","li"]
    )

data = {}

## my_titles는 list 객체
for title in my_titles:
	data[title.text] = title.get('href')
    # ## Tag안의 텍스트
    # print(title.text)
    # ## Tag의 속성을 가져오기(ex: href속성)
    # print(title.get('href'))

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)