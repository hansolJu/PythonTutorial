def PrintStar(charector,size):
    for i in range(size.__len__()):
      print("%s"%charector*size[i])

inputSize = []
charector = input("문자열을 입력하세요")
for i in range(10):
    inputSize.append(int(input("높이를 입력하세요")))
PrintStar(charector,inputSize)