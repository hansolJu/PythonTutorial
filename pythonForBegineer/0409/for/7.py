# 행과 열의 크기를 입력받아 바둑판형태의 2차원 공간의 각 칸마다 행 번호와 열번호를 곱한 값을 출력하시오.
row = int(input("row?= "))
columns = int(input("columns?= "))

for i in range(1,row+1):
    for j in range(1,columns+1):
        print("%d"%(i*j),end='  ')
    print('')