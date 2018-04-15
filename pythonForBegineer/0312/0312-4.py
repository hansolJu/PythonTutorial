anti=int(input("입력 진수 결정(16/10/8/2): "))
input=input("값 입력: ")

if anti==16:
    num10 = int(input,16)
elif anti==10:
    num10=input
elif anti==8:
    num10 = int(input,8)
elif anti==2:
    num10 = int(input,2)
else:
    exit()

print("16진수==> ",hex(num10))
print("10진수==> ",num10)
print("8진수==> ",oct(num10))
print("2진수==> ",bin(num10))