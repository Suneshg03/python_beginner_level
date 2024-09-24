#FIND ALL DIVISORS OF A NUMBER

value=int(input("ENTER THE VALUE:"))

for i in range(1,value+1):
    if value%i==0:
        print("the divisors are:",i)
