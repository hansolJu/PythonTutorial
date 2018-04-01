# 연봉(원 단위)을 숫자로 입력받은 후, 연봉 금액에 대한 소득세를 계산하여 출력하세요.
# 연봉 1천만 원 미만 : 연봉의 9.5%
# 연봉 1천만 원 ~ 4천만원미만 : 연봉의 19%
# 연봉 4천만 원 ~ 8천만원미만 : 연봉의 28%
# 연봉 8천만 원 : 연봉의 37%
# 사용하는 변수는
#           income #연봉 (원 단위)
#           tax #소득세 (원 단위)
income = int(input("연봉을 입력하세요."))
if(income<10000000):
	tax = income*0.095
elif(income>=10000000 and income<40000000):
	tax = income *0.19
elif(income>=40000000 and income<80000000):
	tax = income*0.28
else:
	tax = income*0.37

print("입력한 연봉의 소득세는 %d 입니다." %tax)