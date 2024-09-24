#FIND ARMSTRONG
a=int(input("ENTER THE VALUE:"))
b=str(a)
c=len(b)
d=0
for i in b:
    d=d+int(i)**c

if a==d:
    print(a,"is armstrong")

else:
    print(a,"is not armstrong")
    
