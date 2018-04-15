# 파일용량을 메가바이트 단위로 입력받고, 전송방식을 숫자로 입력받아 파일 전송시간을 초단위로 계산하여 출력하세요.
# WiFi 전송속도 = 1.5MBps / Bluetooth 전송속도 = 300KBps
# LTE 전송속도 = 1MBps / USB 2.0 전송속도 60MBps
# 사용하는 변수는
#     megabytes, bytes #용량 (각각의 단위로)
#     kind #전송방식 (1: WiFi, 2: Bluetooth, 3: LTE, 4: USB 2.0)
#     time #전송시간 (초단위
megabytes = int(input("메가바이트 단위의 용량을 입력하세요.: "))
kind = int(input("전송방식을 입력하세요.(1.Wifi,2:Bluetooth,3:LTE,4:USB2.0) : "))

if(kind==1):
	megabytes/=1.5
elif(kind==2):
	megabytes/=0.3
elif(kind==3):
	megabytes/=1
elif(kind==4):
	megabytes/=60
print(("입력한 값은 %f초 입니다."%megabytes))
