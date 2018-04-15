# 반복해서 0부터 100 사이의 숫자를 입력받아 지금까지 입력된 숫자들 중 가장 큰 수와 가장 작은 수가
# 무엇인지 출력하세요. 범위를 넘으면 종료하게 하세요. 반복은 while 문을 사용하세요.
# 사용하는 변수는
#        number #입력받은 수
#        max_num, min_num #가장 큰 숫자, 가장 작은 숫자
max_num = 0;
min_num = 100;
number = 0;
while (number<100):
    number = int(input("0~100"))
    if(number>max_num):
        max_num = number
    if(number<min_num):
        min_num = number
    print("max_num = ",max_num)
    print("min_num = ",min_num)
