# 046 리스트 reverse
#
# 다음과 같이 날짜로 구성된 리스트가 있을 때 이를 역순으로 정렬하라.
#
# >>> tlist
# ['2016-09-05', '2016-09-06', '2016-09-07', '2016-09-08', '2016-09-09']
#
# 실행 예:
# >>> tlist
# ['2016-09-09', '2016-09-08', '2016-09-07', '2016-09-06', '2016-09-05']
# >>>
tlist = ['2016-09-05', '2016-09-06', '2016-09-07', '2016-09-08', '2016-09-09']
print(sorted(tlist,reverse=1))