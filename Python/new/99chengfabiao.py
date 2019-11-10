a=1
b=1
i=1
j=1
while i<=9 :
    a=i
    while b<=a :
        j=a*b
        print(str(a)+"*"+str(b)+"="+str(a*b),end=" ")
        b+=1
    i+=1
    b=1
    print("")