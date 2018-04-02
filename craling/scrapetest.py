from urllib.request import urlopen
html = urlopen("http://kutis.kyonggi.ac.kr/webkutis/index.jsp")
print(html.read())
