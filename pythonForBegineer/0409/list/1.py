# 10개의 숫자를 입력 받아 리스트에 저장한 후에 이 중에서 두 번째로 큰 수가 몇 번째 숫자 인지 찾아내어 출력하세요.
numList = []
maxNum=0
secondNum=0

for i in range(1,11):
    numList.append(int(input("%d?= " % i)))

numList.sort()

maxNum=max(numList)
secondNum=numList[8]

print(numList[9],numList[8])

