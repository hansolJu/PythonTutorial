# 1부터 100사이의 임의의 숫자를 만들어서 대(70 이상), 중(40이상~70미만), 소(40미만)
# 셋 중에 하나를 판정하여 결과를 리턴하는 함수 GetRandom()을 만드세요.
# 그리고 이 함수를 이용해서 임의의 숫자 10개에 대해
# 대, 중, 소가 각각 몇 번씩 포함되어 있는지 개수를 출력하세요.
import random

def get_random():
    large = 0
    medium = 0
    small = 0
    for i in range(10):
        init = random.randrange(1, 100)
        print(i+1, '생성된 숫자는', init, '입니다.')
        if init>=70:
            large+=1
        elif init>=40 and init<70:
            medium +=1
        elif init<40:
            small+=1
    return print("대 (70이상) :", large, "회 생성\n",
                 "중 (40이상) :", medium, "회 생성\n",
                 "소 (40미안) :", small, "회 생성")

get_random()