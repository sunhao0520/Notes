you=input("请输入你要出的拳")
import random
computer=random.randint(1,3)
if computer==1:
    computer="剪刀"
elif computer==2:
    computer="石头"
else:computer="布"
print("你出的拳是%s,电脑出的拳是%s"%(you,computer))
if ((you=="剪刀" and computer=="布")
        or(you=="石头" and computer=="剪刀")
        or(you=="布" and computer=="石头")):
    print("欧耶 电脑是个垃圾啊")
elif (you==computer):
    print("想一块儿去了")
else:
    print("啊  不服   我要再来一次")


"""
you=input("请输入你要出的拳")
computer="石头"
print("你出的拳是%s,电脑出的拳是%s"%(you,computer))
if ((you=="剪刀" and computer=="布")
        or(you=="石头" and computer=="剪刀")
        or(you=="布" and computer=="石头")):
    print("欧耶 电脑是个垃圾啊")
elif (you==computer):
    print("想一块儿去了")
else:
    print("啊  不服   我要再来一次")
"""


"""
you=input("请输入你要出的拳")
computer="石头"
print("你出的拳是%s,电脑出的拳是%s"%(you,computer))
if (you=="剪刀" and computer=="布") or(you=="石头" and computer=="剪刀") or(you=="布" and computer=="石头"):
    print("欧耶 电脑是个垃圾啊")
elif (you==computer):
    print("想一块儿去了")
else:
    print("啊  不服   我要再来一次")
"""




"""
you=input("请输入你要出的拳")
computer="石头"
print("你出的拳是%s,电脑出的拳是%s"%(you,computer))
if not you==computer:
    if computer=="石头":
        if you=="布":
            print("你赢了")
        else:print("你输了")
    elif computer=="剪刀":
        if you=="布":
            print("你赢了")
        else:print("你输了")
 #   print("做比较")

else:print("你和电脑打了平手")
"""