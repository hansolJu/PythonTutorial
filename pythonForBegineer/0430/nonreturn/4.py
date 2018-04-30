def PrintStar(charector,blank,height):
    for i in range(height):
        for j in range(blank+height):
            print(" ",end='')
        blank-=1
        print("%s"%charector*(i+1))
inputSize = []
charector = input("문자열을 입력하세요")
blank = int(input("공백의 수를 입력하세요"))
height = int(input("높이를 입력하세요"))

PrintStar(charector,blank,height)