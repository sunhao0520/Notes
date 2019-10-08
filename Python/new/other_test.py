def sum_2_num(a,b):
    """"对两个数字的求和"""
    print("%d+%d" % (a, b),end="=")
    return a+b

a=int(input("请输入加数1："))
b=int(input("请输入加数2："))
you =sum_2_num(a,b)
print(you)



def chenfabiao():
    i=0
    j=0
    K=0
    while i<=9:
        while j<=i:
            K=i*j
            print("%d×%d=%d"%(i,j,K),end=" ")
            j+=1
        print(" ")
        j=0
        i+=1