# 숫자 10개를 입력받아 이 중 최댓값을 찾아서 리턴하는 함수 MaxOfTen()을 만들고,
# 이 함수를 이용하여 10개의 숫자 중 최댓값을 출력하세요.

def max_of_ten():
    result = []

    for i in range(10):
        print(i + 1, "번째 수를 입력하세요: ")
        result.append(int(input()))
    result.sort(reverse=1)

    return print("최대값은", result[0], "입니다.")

max_of_ten()
