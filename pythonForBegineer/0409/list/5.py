person=[]
personBmList=[]
count= 0

for i in range(10):
    personInfo=[]
    for j in range(1):
        height = int(input("%d 번째 사람의 신장을 입력하세요(cm 단위):"%(i+1)))
        weight = int(input("%d 번째 사람의 몸무게 입력하세요(kg 단위):"%(i+1)))
        bm = weight/pow((height/100),2)
        # print(bm)
        personInfo.append(height)
        personInfo.append(weight)
    person.append(personInfo)
    personBmList.append(bm)

for i in range(10):
    if(personBmList[i]>25):
        print("%d 번째 사람은 비만 입니다."%(i+1))
        count = count+1;

print("비만인 사람은 총 %d 명 입니다."%count)