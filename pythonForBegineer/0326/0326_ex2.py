# 물의온도를 입력받고, 이 물이 어느 정도의 온수인지 다음과 같이 판정하세요. 
# 음수 (0 미만) : 잘못입력 / 0 ~ 25도 미만 냉수 / 25도 ~ 40도 미만 미온수 
# 40도 ~ 80도 미만 온수/ 80도 이상 끓는 물 혹은 열수 
# 사용하는 변수는 
#          input_degree #입력 온도 
input_degree=int(input("물의 온도를 입력하세요."))
if(input_degree<0):
    print ("잘못입력")
elif(input_degree>0 and input_degree<25):
    print ("냉수")
elif(input_degree>24 and input_degree<40):
    print ("미온수")
elif(input_degree>39 and input_degree<80):
    print ("온수")
elif(input_degree>80):
    print ("열수")
