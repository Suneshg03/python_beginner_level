#FACTORIAL OF A GIVEN NUMBER 
#METHOD 1:USING FOR LOOP
num=int(input("ENTER THE NUMBER:"))
fact=1
for i in range(1,num+1):
    fact=fact*i

print(num,"factorial is",fact)


#MEHOD 2:USING WHILE LOOP
num=int(input("ENTER THE NUMBER:"))
num2=num
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(num2,"factorial is",fact)
    
