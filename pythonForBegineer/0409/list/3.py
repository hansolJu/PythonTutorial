mainSubject=['국어','영어','수학']
jumsuList =[]
totalList=[]
sum =0

for i in range(5):
    personJumsuInfo = []
    for j in range(3):
        personJumsuInfo.append(int(input("%d 번째 학생의 %s 점수를 입력하세요."%(i+1,mainSubject[j-1]))))
    jumsuList.append(personJumsuInfo)

#print(jumsuList)

for j in range(3):
    for i in range(5):
        sum = sum+jumsuList[i][0]
    totalList.append(sum)
    #print(sum)

#print(totalList)
for i in range(3):
    for j in range(1):
        print("%s 과목 총점: %.1f"%(mainSubject[i],totalList[i]))
        print("%s 과목 평균: %.1f"%(mainSubject[i],(totalList[i]/5)))