
"""
name_list=["张三","李四","王五"]
for my_name in name_list:
    print("我的名字是%s"%my_name)
"""
name_list=[{"name":"小美"},
              {"name":"阿土"}]
find_name="呱呱"
for stu_fin in name_list:
    print(stu_fin)
    if stu_fin["name"]==find_name:
        print("找到了   %s"% find_name)
        break
else:
    print("没找到")
print("执行结束")
