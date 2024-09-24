#reverse a number

#METHOD 1

a=int(input("ENTER THE VALUE:"))
b=str(a)
print(b[::-1])


#METHOD2
value=int(input("ENTER THE VALUE"))
reverse=0
while value>0:
    digit=value%10
    reverse=digit+(reverse*10)
    value=value//10
print(reverse)
