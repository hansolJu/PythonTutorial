# 심사점수를 10개 입력 받아 리스트에 저장한 후, 이 중에서 가장 큰 점수와 가장 작은 점수를 제외한 8 개의 점수에 대한 평균을 계산하여 출력하세요.
numList = []
sum=0

for i in range(1,11):
    numList.append(int(input("%d?= " % i)))

numList.sort()

print(numList[1:9])
for i in numList[0:8]:
    print(numList[i])
    sum=sum+numList[i]

print(sum/8)

