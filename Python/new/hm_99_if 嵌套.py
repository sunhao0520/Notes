has_ticket=True
Knife_length=int(input("刀的长度"))
if has_ticket==1:
    if Knife_length>20:
        print("这么长的刀，有%d这么长，你来个锤子"%Knife_length)
    else:print("进吧 进吧  搞快些")
else:print("没票来个锤子")