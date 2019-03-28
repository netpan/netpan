x=input("请输入累加值上限：")
while not str.isdecimal(x):
    print("你是来搞笑的吧，输入数字呀！")
    x = input("请输入累加值上限：")
t=int(x)
i=1
s=0
while i<=t:
    s+=i
    i+=1
print("从1累加到 %d 的结果是 %d" %(t,s))