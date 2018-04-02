from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
	html = urlopen("http://kutis.kyonggi.ac.kr/webkutis/view/indexWeb.jsp")
except HTTPError as e:
	print(e)
	#null
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj)
