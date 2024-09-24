#fibonacci series if else condition

count=int(input())
num1=0
num2=1
iteration=0
if(count<=0):
    print("the count has greater than 0")

else:
    print("the fibonacci series",end="")
    while(iteration<count):
        print(num1,end=",")
        nextnum=num1+num2
        num1=num2
        num2=nextnum
        iteration=iteration+1

        
