mode = int(input("mode?="))

if mode==1:
    for i in range(1,5):
        for j in range(1,10):
            print("%d * %d = %d"%(2*i+1,j,(2*i+1)*j),end='  ')
            if(j%3==0):
                print("")
        print('')
elif mode==2:
    for i in range(1,5):
        for j in range(1,10):
            print("%d * %d = %d"%(2*i,j,(2*i)*j),end='  ')
            if(j%3==0):
                print("")
        print('')
else:
    exit()