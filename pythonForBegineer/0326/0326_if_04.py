# 가족이 총 몇 명인지 입력받고, 각각의 태어난 년도를 입력받으면서 미성년자의 수를 계산해 출력하세요.
# 반복은 for 문을 사용하세요.
# 나이 = “2018 – 태어난 년도 + 1” 로 계산 하고, 20세 미만은 미성년자로 판정합니다.
# 사용하는 변수는
#       count_all #가족구성원 수
#       count_young #미성년자의 수
#       birth_year #태어난 년도
#       age #나이
#       index #반복문 사용을 위한 변수
count_all =0
count_young =0
birth_year=0
age=0
index=0

count_all = int(input("가족인원수: "))
for index in range(count_all):
    birth_year=int(input("태어난년도: "))
    age = 2018 -birth_year +1
    if(age<20):
        count_young+=1
print(count_young)