# 반복해서 0부터 100 사이의 숫자를 입력받아 지금까지 입력된 숫자들의 개수와
# 숫자들의 총 합, 평균을 출력하세요 범위를 벗어나면 종료하세요. 반복은 while 문을 사용하세요.
# 사용하는 변수는
#     number #입력받은 수
#     count #입력받은 숫자의 개수
#     totalsum #총합계
#     average #평균
number = 0
count = 0
totalsum = 0
average = 0
while (number<100):
    number = int(input("0~100사이의 수"))
    count +=1
    totalsum +=number
    average = totalsum/count
    print("총합: %d, 평균: %d"%(totalsum,average))
