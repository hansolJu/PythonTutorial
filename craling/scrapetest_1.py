from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://kutis.kyonggi.ac.kr/webkutis/view/indexWeb.jsp")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.div)