# 숫자를 한 개 입력받은 후에 그 숫자의 높이를 가지는 직각삼각형을 “ * “ 문자로 화면에 출력하세요. 예를 들어 3이 입력되면
#
# *
# **
# ***      와 같은 형태로 출력되어야 합니다.
#
# 사용하는 변수는
#      height       #출력하려는 삼각형의 높이
height = int(input("숫자를 입력하세요."))

for i in range(1,height+1):
    for j in range(0,i):
        print("*",end='')
    print('')