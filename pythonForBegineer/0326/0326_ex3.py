# 직사각형의 가로길이와 세로길이를 입력받아서 면적을 계산하고, 그 모양을 판정하세요.
# 직사각형 넓이는 “가로길이*세로길이” 로 하면 됩니다.
# 평가는 다음과 같이 합니다. 중복되는 경우가 아닌 1가지 경우만 출력합니다.
# 가로 길이와 세로길이가 같으면 : 정사각형
# 가로길이가 세로길이보다 2배 이상이면 : 좌우로 길쭉한 직사각형
# 반대로 세로길이가 2배 이상이면 : 위아래로 길쭉한 직사각형
# 가로길이가 길면 : 일반적인 가로형 직사각형
# 세로길이가 길면 : 일반적인 세로형 직사각형
# 사용하는 변수는
#          width, height #가로길이, 세로길이
#          area #
width = int(input("가로 길이를 입력하세요."))
height = int(input("세로 길이를 입력하세요."))
area = width*height
print("면적은 %d입니다."%area)

if(width==height):
    print("정사각형")
elif(width>height*2):
    print("좌우로 길쭉한 직사각형")
elif(height>width*2):
    print("위아래로 길쭉한 직사각형")
elif(width>height):
    print("일반적인 가로형 직사각형")
elif(width<height):
    print("일반적인 세로형 직사각형")