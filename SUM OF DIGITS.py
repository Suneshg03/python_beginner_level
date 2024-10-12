#SUM OF DIGITS
#METHOD 1:USING FOR LOOP

num1=int(input("ENTER THE NUMBER:"))
sum1=0
for i in str(num1):
    sum1=sum1+int(i)
print("the sum is:",sum1)


               
#METHOD 2:USING WHILE LOOP

num1=int(input("ENTER THE NUMBER:"))
sum1=0
while num1>0:
    last_digit=num1%10
    sum1=sum1+last_digit
    num1=num1//10
print("the sum is:",sum1)
