row=1
col=1
K=0
while row<=9:
    while col<=row:
        K=col*row
        print("%d×%d=%d\t"%(col,row,K),end=" ")
        col+=1
    print(" ")
    col=1
    row+=1

print("")
import other_test
other_test.chenfabiao()

"""
i=0
j=0
k=0
number=0
while i<=9:
    while j<=i:
        k=i*j
        #让他该换行时候才换行，不换行时就不换行
        if  i==j:
            print("%d×%d=%d" %(j,i,k))
        else:
            print("%d×%d=%d" %(j,i,k),end=" ")
        number+= 1 #运算次数统计
        j+= 1
    j = 1 #每次要把J归1再重新算一遍
    i+= 1
print("一共运算了%d次"%number)

#其乐无穷
"""



"""
#小星星
i=0
while i<=5:
    print("*"*i)
    i+= 1
"""