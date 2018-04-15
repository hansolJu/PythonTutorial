# 국어, 영어, 수학
# 점수를
# 입력받아
# 이
# 점수의
# 총점과
# 평균을
# 계산하세요.
# 총점은 “국어점수 + 영어점수 + 수학점수”,
# 평균은 “총점 / 3.0” 으로
# 하면
# 됩니다. 
# 사용하는
# 변수는
# kor, eng, math  # 과목 점수
# total  # 총점
# average  # 평균점수
kor=float(input("국어: "))
eng=float(input("영어: "))
math=float(input("수학: "))
total= kor+eng+math
average = total/3.0
print(total)
print(average)