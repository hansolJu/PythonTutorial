# 039 문자열 개수 확인
#
# 'Python python pYthon java Java'에서 대소문자를 구분하지 않고 사용된 python 문자열의 개수를 출력하라.
str = 'Python python pYthon java Java'
str = str.lower()
print(str.count('python'))
