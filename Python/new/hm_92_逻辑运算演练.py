"""
年轻在0-120之间就合格
age=int(input("请输入年龄"))
if age>0 and age<120:
    print("条件成立")
else: print("条件不成立")
"""
#只要有一门大于60就合格
python_score=int(input("请输入python分数"))
c_score=int(input("请输入C语言分数"))
if python_score>60 or c_score>60:
    print("分数合格")
else: print("分数不合格")