def AskBiman(height,weight):
    biman = weight/pow((height/100),2)

    if(biman < 18.5):
        print("저체중입니다.")
    elif(biman>=18.5 and biman<23):
        print("정상체중입니다.")
    elif(biman>=23 and biman<25):
        print("과체중입니다.")
    elif (biman >= 25 and biman < 30):
        print("경도비만입니다.")
    elif (biman >= 30):
        print("고도비만입니다.")
    else:
        print("무언가 오류가 발생.")
        exit()

for i in range(5):
    height = int(input("%d번째 사람의 신장을 입력하세요: "%i))
    weight = int(input("%d번째 사람의 몸무게를 입력하세요:"%i))
    AskBiman(height,weight)