# 010 거듭제곱
#
# 사용자로부터 밑과 지수를 입력 받은 후 거듭제곱 값을 출력하라.
#
# 실행 예:
# 밑: 3
# 지수: 2
# 3^2 = 9

print("밑: ", end="")
base = int(input())
print("지수: ", end="")
exponentiation = int(input())
print(base, "^", exponentiation, "=", pow(base, exponentiation))
  