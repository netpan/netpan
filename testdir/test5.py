a=range(2,10)
for i in a:
    for j in range(2,i):
        if i % j == 0:
            print("%d = %d * %d" %(i,j,i//j))
            break
    else:
        print("%d 是一个素数" %i)