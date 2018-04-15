# 아파트 분양면적을 제곱미터(𝑚2)로 받아 평형(x평) 단위로 변환하고, 그 크기를 판정하세요.
#
# 평형계산은 제곱미터/3.305 로 하면 됩니다.
# 평가는 다음과 같습니다.
# 15평 미만 : 소형 / 15평 ~ 30평미만 : 중소형 / 30평 ~ 50평 미만 : 중형
# 50평 이상 : 대형
# 사용하는 변수는
#          m2_area #면적(제곱미터)
#          pyung_area #면적(평수)
m2_area=int(input("분양 면적을 입력하세요."))
pyung_area=m2_area/3.305
print("%d평 입니다."%(pyung_area))

if(pyung_area<15):
    print("소형")
elif(pyung_area>15 and pyung_area<30):
    print("중소형")
elif(pyung_area>29 and pyung_area<50):
    print("중형")
elif(pyung_area>50):
    print("대형")