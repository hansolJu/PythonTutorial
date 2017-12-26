# 040 문자열 분리
#
# 사용자로부터 '10:00:01'와 같은 형태로 시간을 입력 받은 후 해당 시간이 00:00:00 으로부터 몇 초가 지났는지를 출력하라.
#
# time: 10:00:01
# 36001

time = input('time: ')
time = time.split(':')
time = int(time[0])*3600+int(time[1])*60+int(time[2])
print(time)
