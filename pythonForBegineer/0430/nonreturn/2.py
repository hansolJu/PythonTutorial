def PrintStar(size):
    for i in range(size.__len__()):
      print("*"*size[i])

inputSize = []

for i in range(10):
    inputSize.append(int(input("높이를 입력하세요")))
PrintStar(inputSize)