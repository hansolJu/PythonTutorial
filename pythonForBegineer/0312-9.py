# 날 수를 입력받아 이 날수에 해당하는 기간은 모두 몇 초인지 계산하세요.
#  초 계산은 “날수 * 24 * 60 * 60” 로 하면 됩니다. 
#  사용하는 변수는
#       days  #날수
#       seconds #초단위 시간
days = int(input("날 수를 입력하세요: "))
seconds = days*24*60*60
print(seconds)
