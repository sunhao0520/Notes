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
    find_name=input("请输入你要查询的名字：")
    # 遍历名片夹，输出内容
    for card_dict in card_list:
        if card_dict["name"]==find_name :
            for name_m in ["姓名", "电话", "企鹅号", "邮箱"]:
                print("%-s"% name_m , end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq_number"],
                                            card_dict["mail"]))
            deal_card(card_dict)
            #对后序代码进行修改或添加
            return
    print("输入的名字不对，请重新输入，或按1创建")

def deal_card(find_dict):
    """修改名片
    find_dict 前面需要修改的名片
    """
    keyword_deal=input("请输入你要对名片进行什么操作 "
                       "r-修改 d-删除 0-返回上级菜单\n选择：")
    # 修改名片
    if keyword_deal=="r" or keyword_deal=="R":
        #for r_card in deal_card(find_dict):
        #print("姓名",end="")
        find_dict["name"]=input_card(find_dict["name"],"姓名")
        find_dict["phone"]=input_card(find_dict["phone"],"电话")
        find_dict["qq_number"]=input_card(find_dict["qq_number"],"QQ号码")
        find_dict["mail"]=input_card(find_dict["mail"],"邮箱")
        #print("修改姓名成功")
    # 删除名片
    elif keyword_deal == "d" or keyword_deal == "D":
        card_list.remove(find_dict)

    elif keyword_deal == "0":
        return
    else:
        print("请输入r或d,或选0退出")

def input_card(dict_value,tip_message):
    """输入修改，回车则不修改
    dict_value 源数据
    tip_message 提示
    return 如果长度为0，返回名片源数据，长度不为0，返回输入值
    """
    #1 提示用户输入
    print(tip_message,end="")
    input_cards=input("修改为")
    #2针对用户的输入进行判断
    if len(input_cards)==0:
        print("%s 不修改" % tip_message)
        return dict_value
    else:
        print("%s 已修改完成"%tip_message)
        return input_cards