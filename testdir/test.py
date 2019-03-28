a=int(input("请输入你家狗儿的年龄："))
if a<0:
    print("你是来搞笑的吧！")
elif a==1:
    print("相当于人类14岁的年龄！")
elif a==2:
    print("相当于人类22岁的年龄！")
else:
    b=22+(a-2)*5
    print("相当于人类 %d 岁的年龄" %(b))
input("press enter to exit!")