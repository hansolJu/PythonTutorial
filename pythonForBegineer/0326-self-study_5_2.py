## 두 숫자 사이의 합계를 구하는 프로그램을 만들어보자. 단1씩 증가하지 않고 증가하는 숫자도 입력받는다. 예를들어1,100,3을입력하면1+4+.....+100의합계를구한다.
answer = 0;
num = int(input("***  첫번 째 숫자 를 입력하세요 : "))
num2 = int(input("***  두번 째 숫자 를 입력하세요 : "))
count = int(input("***  더할 숫자를 입력하세요 : "))

for i in range(num,num2+1,count):
    answer = answer+i
print("%d.....%d는 %d입니다."%(num,num2,answer))
