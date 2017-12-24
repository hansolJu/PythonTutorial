# 009 사칙 연산
#
# 사용자로부터 두 개의 숫자를 입력 받은 후 두 숫자의 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 결괏값을 출력하라.
#
# 실행 예:
# first number: 10
# second number: 2
# add:  12
# sub:  8
# mul:  20
# div:  5.0
print("first number: ", end="")
first = int(input())
print("second number: ", end="")
second = int(input())
print("add: ", first + second)
print("sub: ", first - second)
print("mul: ", first * second)
print("div: ", first / second)
