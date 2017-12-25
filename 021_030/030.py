# 030 문자열 분리
#
# 다음 문자열에 대해 문자열 길이를 기준으로 두 부분으로 분리하여 출력하라.
#
# letters = "introducing python"
#
# 실행 예:
# 'introduci'
# 'ng python'
letters = "introducing python"
str_length = len(letters)
half = int(str_length/2)
print(letters[:half])
print(letters[half:])