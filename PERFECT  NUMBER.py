num=int(input("ENTER ANY NUMBER:"))
sum1=0
for i in range(1,num):
    if num%i==0:
        sum1=sum1+i

if num==sum1:
    print("perfect number")

else:
    print("not perfect number")
