# 숫자 2개와 연산기호 문자 (“+”, “-”, “*”, “/”) 하나를 입력 받아 첫 번째 입력숫자와
# 두 번째 입력숫자 사이에 해당 기호를 넣은 연산결과를 수행하세요.
# 사용하는 변수는
#          num1, num2 #숫자 2개
#          operator #연산기호 (“+”, “-”, “*”, “/”)
#          result #결과
num1 = int(input("첫번째 수를 입력하세요.: "))
num2 = int(input("두번째 수를 입력하세요.: "))
operator = input("연산자를 입력하세요.(“+”, “-”, “*”, “/”): ")

if(operator == '+'):
	result = num1+num2
elif(operator == '-'):
	result = num1 - num2
elif(operator == '*'):
	result = num1 * num2
elif(operator == '/'):
	result = num1/num2
else:
	print("error")
	exit()
print("입력한 연산의 결과는 %d 입니다."%result)

