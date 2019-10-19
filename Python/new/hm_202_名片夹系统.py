"""
**************************************************
欢迎使用【名片管理系统】V1.0

1. 新建名片
2. 显示全部
3. 查询名片

0. 退出系统
**************************************************
"""
#无限循环

import hm_202_名片夹执行工具
while True:
    #功能菜单显示
    hm_202_名片夹执行工具.show_menu()
    #下面是定义功能
    action_str=input("请选择希望执行的操作:")
    print("你选择执行的操作是:%s"%action_str)
    word=["1","2","3"]
    #1. 新建名片 2. 显示全部 3. 查询名片
    if action_str in word:
        #1新建名片
        if action_str=="1":
            hm_202_名片夹执行工具.new_card()
        #2显示全部
        elif action_str=="2":
            hm_202_名片夹执行工具.show_all()
        #3查询名片
        elif action_str=="3":
            hm_202_名片夹执行工具.search_card()
        print(" ")
    #0. 退出系统
    elif action_str=="0":
        print("你已退出系统,欢迎下次使用")
        break
    #输入错误
    else:
        print("你输入错误，请按提示输入")
