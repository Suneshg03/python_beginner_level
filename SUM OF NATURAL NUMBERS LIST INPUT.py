#METHOD 1:SUM NATURAL NUMBERS USING NESTED FOR LOOP

num=[1,2,3,4,5]
for i in num:
    sum1=0
    for j in range(1,i+1):
        sum1=sum1+j
    print(i,"=",sum1)



#METHOD 2:FINDING SUM OF NATURAL NUMBERS IN A EMPTY LIST

num=[]
while True:
    add=input("ENTER A VALUE:")
    if add=="done":
        break
    num.append(add)

for i in num:
    sum1=0
    for j in range(1,int(i)+1):
        sum1=sum1+j
    print(i,"=",sum1)

