from typing import List, Any

mainSubject=['국어','영어','수학']
jumsuList =[]
totalList=[]
averageList=[]
sum =0
# 5 명의 학생 점수를 입력 받는 부분
for i in range(5):
    personJumsuInfo = []
    for j in range(3):
        personJumsuInfo.append(int(input("%d 번째 학생의 %s 점수를 입력하세요."%(i+1,mainSubject[j-1]))))
    jumsuList.append(personJumsuInfo)

#print(jumsuList)
# 3과목 총점 계산 부분
for i in range(5):
    for j in range(3):
        sum = sum+jumsuList[i][j]
    totalList.append(sum)

for i in range(5):
    print("%d 번째 학생의 총점은: %d, 평균은: %.1f 입니다."%(i+1,totalList[i],totalList[i]/3))