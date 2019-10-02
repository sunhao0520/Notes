def sum_2_num(a,b):
    """"对两个数字的求和"""
    c=a+b
    print("%d+%d=%d"%(a,b,c))

a=int(input("请输入加数1："))
b=int(input("请输入加数2："))
sum_2_num(a,b)




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