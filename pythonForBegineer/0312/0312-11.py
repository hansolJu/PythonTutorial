# 파일용량을
# 기가바이트
# 단위로
# 입력받아
# 메가
# 바이트, 킬로
# 바이트, 바이트
# 단위
# 로
# 계산해
# 각각
# 출력하세요.
# 메가바이트 = 기가바이트 * 1024
# 식으로
# 계산합니다.
# 기가 > 메가 > 킬로 > 바이트
# 사용하는
# 변수는
# gigabytes, megabytes, kilobytes, bytes  # 용량 (각각의 단위로)
giga = int(input("기가 바이트로 입력하세요: "))
megabytes = giga*1024
kilobytes = megabytes*1024
bytes = kilobytes*1024

print(megabytes)
print(kilobytes)
print(bytes)