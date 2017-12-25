# 029 도메인 추출
#
# 사용자로부터 웹 페이지 주소를 입력 받은 후 도메인을 출력하라. 도메인은 .com, .net, .org 만 지원한다. www는 반드시 입력된다.
#
# 실행 예:
# address: http://www.wikidocs.net/edit/page/7022
# domain: net
url = input("address: ")
domain = url.split('.')[2][:3]
print("domain: ", domain)