number=20
guess=-1
while guess!= number:
    tmd=input("请输入一个数字")
    if not str.isdecimal(tmd):
        print("请输入数字哦，输入字母不行哦！")
        continue
    guess=int(tmd)
    if guess>20:
        print("大了哦！")
    elif guess<20:
        print("小了哦！")
print("你太棒了！")