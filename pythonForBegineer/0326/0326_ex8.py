# 3개의 숫자를 입력받아 이 숫자들 중 가장 큰수와 가장 작은 수를 출력하세요.
# 사용하는 변수는
#      num1, num2, num3 #각각의 숫자
#      max_num, min_num #가장 큰 숫자 가장 작은 숫자

num1 = int(input("첫번째 수를 입력하세요."))
num2 = int(input("두번째 수를 입력하세요."))
num3 = int(input("세번째 수를 입력하세요."))

if(num1>num2):
	if(num2>num3):
		max_num = num1
		min_num = num3
	elif(num3>num1):
		max_num=num3
		min_num=num2
else:#num2>num1
	if(num1>num3):
		max_num = num2
		min_num = num3
	elif(num3>num2):
		max_num=num3
		min_num=num1

print("가장 큰수 :",max_num)
print("가장 작은수: ",min_num)