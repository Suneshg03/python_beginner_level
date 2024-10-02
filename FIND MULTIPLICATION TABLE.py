#FIND MULTIPLICATION TABLE

#METHOD 1:USING FOR LOOP
num=int(input("ENTER TABLE NUMBER:"))
num2=int(input("ENTER THE NUMBER:"))
for i in range(1,num2+1):
    print(f"{i} x {num} ={num*i}")


#METHOD 2:USING WHILE LOOP
    
num=int(input("ENTER THE TABLE NUMBER:"))
num1=int(input("ENTER THE NUMBER:"))
i=1
while i<=num1:
    print(f"{i} x {num} ={i*num}")
    i=i+1
