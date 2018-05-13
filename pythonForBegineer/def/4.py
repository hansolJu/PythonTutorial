# 자판기의 메뉴를 보여주고 선택하게 하여 선택된 음료의 가격을 리턴하는 함수 SelectCan()을 만드세요.
# 그리고 이 함수를 이용해서 자판기에서 음료를 반복해서 선택하게 하여 총 음료의 개수와 가격을 출력하세요.
#  반복 유무는 Y/N 입력을 통해 확인합니다.
# 1.콜라(700원) 2.원두커피(300원) 3.레몬주스(1000원) 4.홍차(500원) 5.코코아(600원)

def SelectCan():
    sum = 0
    count = 0
    while(1):
        print("1.콜라(700원) 2.원두커피(300원) 3.레몬주스(1000원) 4.홍차(500원) 5.코코아(600원)")
        order=int(input("메뉴를 선택하세요."))
        if order==1:
            sum +=700
            count+=1
        elif order==2:
            sum +=300
            count+=1
        elif order==3:
            sum+= 1000
            count+=1
        elif order==4:
            sum+=500
            count+=1
        elif order==5:
            sum+=600
            count+=1
        else:
            print("잘못 선택 하였습니다. 다시 선택하세요 :ㅇ")

        while(1):
            print("더 필요하십니까? (Y,N)")
            order = input()
            if order== 'Y' or order == 'y':
                break
            elif order=='N' or order == 'n':
                return print(count, "개를 주문하여 총",sum, "원 입니다.")
            else:
                print("잘못 입력하셨습니다. y 와 n 중 선택하여 주십시오.")
                continue

SelectCan()