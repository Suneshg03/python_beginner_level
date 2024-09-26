#METHOD 1:EVEN OR ODD
num=int(input("ENTER THE NUMBER:"))
if num%2==0:
    print(num,"is even")

else:
    print(num,"is odd")

#METHOD 2:EVEN OR ODD IN A RANGE
num=int(input("ENTER THE NUMBER:"))
for i in range(1,num+1):
    if i%2==0:
        print(i,"is even")

    else:
        print(i,"is odd")
    

    
