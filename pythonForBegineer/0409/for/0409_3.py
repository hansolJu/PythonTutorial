height = int(input("숫자를 입력하세요."))

for i in range(1,height+1):
    for k in range(height+1,i,-1):
        print('#',end='')
    for j in range(0,i):
        print("*",end='')
    print('')