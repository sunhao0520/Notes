card_list = [{"name": "老王",
                 "phone": "1232344",
                 "qq_number": "qq111",
                 "mail":"23727@qq.com"},
             {"name": "你好",
              "phone": "12de32344",
              "qq_number": "qq1dede11",
              "mail": "dew23727@qq.com"}]


def show_menu():
    # 功能显示
    print("*" * 50)
    print("1. 新建名片 \n2. 显示全部 \n3. 查询名片\n\n0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 30)
    print("新增名片")
    # 1.提示输入用户名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入手机号：")
    qq_number_str = input("请输入QQ号码：")
    email_str= input("请输入邮件地址：")
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq_number": qq_number_str,
                 "mail":email_str}
    # 将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 提示用户输入成功
    print("添加 %s 的名片成功" % name_str)


def show_all():
    """显示名片"""
    print("-" * 30)
    print("显示名片")
    if len(card_list)==0:
        print("当前没有名片，请按1添加")
        return
    else:
        # 打印表头和分割线
        for name in ["姓名", "电话", "QQ号", "邮箱"]:
            print(name, end="\t\t")
        print("")
        print("-" * 50)
        # 遍历名片列表依次输出字典信息
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq_number"],
                                            card_dict["mail"]))
    #


def search_card():
    """搜索名片"""
    print("-" * 30)
    print("搜索名片")
    #输入你要查询的名字
    name=input("请输入你要查询的名字：")
    # 遍历名片夹，输出内容
    for card_dict in card_list:
        if card_dict["name"]==name :
            for name_m in ["姓名", "电话", "企鹅号", "邮箱"]:
                print("%-s"% name_m , end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq_number"],
                                            card_dict["mail"]))
            return
    print("名字不对，请重新输入，或按1创建")

