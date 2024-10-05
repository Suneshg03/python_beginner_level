#SUM OF THREE GIVEN INTEGERS HOWEVER,IF TWO VALUES ARE EQUAL SUM WILL BE ZERO

#METHOD 1:USER INPUT
num1=int(input("ENTER FIRST NUMBER:"))
num2=int(input("ENTER SECOND NUMBER:"))
num3=int(input("ENTER THIRD NUMBER:"))
if num1==num2 or num2==num3 or num1==num3:
    print("the sum is:0")

else:
    print("the sum is:",num1+num2+num3)




#METHOD 2:USING FUNCTION

def sum_three(x,y,z):
    if x==y or y==z or x==z:
        sum=0


    else:
        sum=x+y+z

    return sum


print(sum_three(2,1,2))
print(sum_three(3,2,2))
print(sum_three(2,2,2))
print(sum_three(1,2,3))
