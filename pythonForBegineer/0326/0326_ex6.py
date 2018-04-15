# 국어, 영어, 수학 점수를 입력받아 이 점수의 총점과 평균을 계산하고, 평균 점수에 따라 등급을 정하여 출력하세요. (수, 우, 미, 양, 가)
# 90이상 : 수 / 80 ~ 90미만 : 우 / 70 ~ 80미만 : 미 / 60 ~ 70 미만 : 양
# 60미만 : 가
# 총점은 “국어점수 + 영어점수 + 수학점수”, 평균 “총점/3.0” 으로 하면 됩니다.
# 사용하는 변수는
# kor, eng, math 과목 점수
#         total 총점
#         average 평균점수
kor=int(input("국어점수를 입력하세요.: "))
eng = int(input("영어 점수를 입력하세요.: "))
math = int(input("수학 점수를 입력하세요.: "))
total = kor+eng+math
average = total/3

print("총점은 %d입니다."%total)
print("평점은 %d입니다."%average)

if(average>89):
	print("수")
elif(average>79 and average<90):
	print("우")
elif(average>79 and average<80):
	print("미")
elif(average>69 and average<70):
	print("양")
elif(average<60):
	print("가")