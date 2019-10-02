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