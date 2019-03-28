def fib(x):
    a,b,n=0,1,0
    while n<x:
        yield b
        a,b=b,a+b
        n+=1
f=fib(6)
for i in f:
    print(i)
for j in fib(7):
    print(j)