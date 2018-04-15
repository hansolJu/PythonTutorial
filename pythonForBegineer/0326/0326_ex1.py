# 태어난 년도를 입력 받고, 이 입력 값으로 나이에 따라 유아, 어린이, 청   소년, 청년, 중년, 노년 여부를 판정하여 출력하세요.
# 나이 계산은 “2018 – 태어난 년도 + 1” 로 하면 되고, 판정은 다음과 같   이 합니다
# 7세 미만 유아/ 7세 ~ 13세 미만 어린이/ 13세 ~ 20세 미만 청소년
# 20세 ~ 30세 미만 청년/ 30세 ~ 60세 미만 중년 / 60세 이상 노년
# 사용하는 변수는
#          birth_year #태어난 년도
#          age #나이
birth_year=int(input("태어난 년도를 입력하세요: "))
age = 2018 -birth_year +1
if(age<7):
    print ("유아")
elif (age>7 and age<13):
    print ("어린이")
elif (age>12 and age<20):
    print("청소년")
elif (age>19 and age<30):
    print("청년")
elif (age>29 and age<60):
    print("중년")
elif (age>59):
    print("노년")