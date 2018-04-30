def PrintMenu():
    sum = 0
    while(1):
        inputNumber=int(input("1.피자(15000원), 2.스파게티(10000원), 3.샐러드(7000원), 4.음료수(2000원), 5.종료\n 메뉴를 선택하세요."))
        if(inputNumber == 1):
            sum += 15000
        elif(inputNumber==2):
            sum += 10000
        elif(inputNumber ==3):
            sum += 7000
        elif(inputNumber==4):
            sum += 2000
        elif(inputNumber==5):
            exit()
        print("현재까지 주문 금액은 %d 원 입니다."%sum)


PrintMenu()