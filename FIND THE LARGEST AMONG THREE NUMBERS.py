#FIND THE LARGEST AMONG THREE NUMBERS
num1=int(input("ENTER THE FIRST NUMBER:"))
num2=int(input("ENTER THE SECOND NUMBER:"))
num3=int(input("ENTER THE THIRD NUMBER:"))

if num1>num2 and num1>num3:
    print(num1,"is largest number")

elif num2>num1 and num2>num3:
    print(num2,"is largest number")

else:
    print(num3,"is largest number")

      
