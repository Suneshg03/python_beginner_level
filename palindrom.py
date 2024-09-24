#PALINDROM:

#METHOD1
value=int(input("ENTER THE VALUE:"))
value2=value
rev=0
while value>0:
    digit=value%10
    rev=rev*10+digit
    value=value//10
if value2==rev:
    print(rev,"is PALINDROM")


else:
    print(rev,"is NOT PALINDROM")


#METHOD2
value=input("ENTER THE VALUE:")
value2=value[::-1]
if value==value2:
    print(value,"is PALINDROM")

else:
    print(value,"is NOT PALINDROM")
