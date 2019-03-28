def printme(a,*b):
    a**=2
    print(a)
    for i in b:
        print(i)
printme(4)
printme(4,5,6,7)