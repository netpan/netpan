x=input("请输入累加值上限：")
while not str.isdecimal(x):
    print("你是来搞笑的吧，输入数字呀！")
    x = input("请输入累加值上限：")
t=int(x)
s=0
for i in range(1,t+1):
    s+=i
print(s)