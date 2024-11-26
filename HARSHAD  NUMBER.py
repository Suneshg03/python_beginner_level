num=int(input("ENTER ANY NUMBER:"))
num2=0
for i in str(num):
    num2=num2+int(i)

if num%num2==0:
    print("Harshad number")

else:
    print("not Harshad number")
