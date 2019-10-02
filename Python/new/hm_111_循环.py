#0-100之间偶数求和
i=0
number=1
sum=0
while i<100:
    if number%2== 0:
        sum = sum + number
        print(number)
    number += 1
    i += 1
print(sum)
print(number)
print("运算了 %d 次"%i)


"""
#0-100之间的累加求和
i=0
number=1
sum=0
while i<100:
    sum=sum+number
    number += 1
    i+= 1
print(sum)
print(number)
print("运算了 %d 次"%i)
"""

"""
i=0
while i<5:
    print("hello python")
    i=i+1
print(i)
"""