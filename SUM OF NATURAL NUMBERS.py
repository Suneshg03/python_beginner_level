#SUM OF NATURAL NUMBERS
#METHOD 1:USING FOR LOOP
num=int(input("ENTER A NUMBER:"))
sum1=0
for i in range(1,num+1):
    sum1=sum1+i
print("the sum is:",sum1)


#METHOD 2:USING WHILE LOOP
num=int(input("ENTER A NUMBER:"))
sum1=0
while num>0:
    sum1=sum1+num
    num=num-1

print("the sum is",sum1)
