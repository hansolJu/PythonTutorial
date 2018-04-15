# 숫자를 입력받은 후 이 숫자가 1보다 큰 경우 1부터 이 숫자까지의 모든 정수를 더한 값을 출력하세요.
# 수열의 합 공식 쓰지 말고, 반복은 for 문으로 하세요.
# 사용하는 변수는
#         number #입력받은 수
#         totalsum #1부터 더한 결과값의 수
#         index #반복문 사용을 위한 변수
number = int(input("입력받은 수"))
totalsum = 0
if(number>1):
    for i in range (number+1) :
        totalsum+=i
print(totalsum)