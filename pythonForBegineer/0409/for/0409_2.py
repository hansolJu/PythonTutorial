# 숫자를 한개 입력받은 후에 그 숫자의 높이를 가지는 정사각형을 "#” 문자로 화면에 출력하세요. 예를 들어 3이 입력되면
#
# # # #
# # # #
# # # #    와 같은 형태로 출력되어야 합니다.
#
# 사용하는 변수는
# 	length    #출력하려는 정사각형 한 변의 길이
length=int(input("length?="))

for i in range(1,length+1):
    for j in range(0,length+1):
        print("#",end='')
    print('')