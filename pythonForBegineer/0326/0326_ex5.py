# 날짜를 월과 일로 입력 받아 입력 받은 날짜는 1년 중 몇 번째 날에 해당되는지 계산하여 출력하세요.
# 매 월의 날 수는 다음과 같이 정의합니다.
# 2월 : 28일
# 1, 3, 5, 7, 8, 10, 12 월 : 31일 /  4, 6, 9, 11월 : 30일
# 월수나 일수 입력이 범위를 초과하면 잘못 입력됐다고 출력하세요.
# 사용하는 변수는
#          month, days # 월, 일
#          day_count #1년중 날 수 
month = int(input("월을 입력해주세요.: "))
days = int(input("일을 입력해주세요.: "))
day_count=days

for i in range(1,month,1):
    if(i==1or i==3or i==5or i==7or i==8or i==10or i==12):
        day_count+=31
    elif(i==4or i==6or i==9 or i==11):
        day_count+=30
    elif(i==2):
        day_count+=28

print("입력하신 날짜는 1년중 %d 번째 날입니다."%day_count)