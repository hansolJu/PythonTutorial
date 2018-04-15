number = [[101,102,103],[201,202,203],[301,302,303],[401,402,403],[501,502,503]]
ho=[]
total = 0

for i in range(5):
    hoNumber=[]
    for j in range(3):
        livingPerson=int(input("%d 호에 거주자수는 몇명인가요?"%number[i][j]))
        hoNumber.append(livingPerson)
        total = total+livingPerson
    ho.append(hoNumber)

print(ho)
print(" 총 거주자 수는 %d 명 입니다."%total)