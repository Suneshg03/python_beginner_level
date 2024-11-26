a=int(input("ENTER ANY NUMBER:"))
a1=a
b=0

while a>0:
    digit=a%10
    fact=1
    while digit>0:
        fact=fact*digit
        digit=digit-1
        
    b=b+fact
    a=a//10


if a1==b:
    print("strong number")

else:
    print("not strong number")
