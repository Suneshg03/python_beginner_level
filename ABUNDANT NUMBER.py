num=int(input("ENTER ANY NUMBER:"))
num2=0
for i in range(1,num):
    if num%i==0:
        num2=num2+i


if num2>num:
    print("Abundant number")

else:
    print("not Abundant number")
