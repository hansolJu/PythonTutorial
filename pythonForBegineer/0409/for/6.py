# 출력 모드 (홀수:1, 짝수:2)와 열 개수를 입력 받아 이에 따라 홀수 단 혹은 짝수 단의 구구단을 1줄에 입력 받은 열 개수만큼 출력하세요.

mode = int(input("mode?="))
column = int(input("column?="))

if mode==1:
    for i in range(1,5):
        for j in range(1,10):
            print("%d * %d = %d"%(2*i+1,j,(2*i+1)*j),end='  ')

            if(j%column==0):
                print("")

        print('')
elif mode==2:
    for i in range(1,5):
        for j in range(1,10):
            print("%d * %d = %d"%(2*i,j,(2*i)*j),end='  ')

            if(j%column==0):
                print("")

        print('')
else:
    exit()