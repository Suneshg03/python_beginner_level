#CHECK FIRST AND LAST NUMBER OF A LIST IS SAME OR NOT

#METHOD 1:FIXED VALUE

lst=[1,2,3,4,5,1]
if lst[0]==lst[-1]:
    print("the result is True")

else:
    print("the result is False")



#METHOD 2:USER INPUT

lst=[]
num=int(input("REQUIRED NUMBERS:"))
for i in range(num):
    num1=int(input("ENTER VALUE:"))
    lst.append(num1)
print(lst)

lst=[1,2,3,4,5,1]
if lst[0]==lst[-1]:
    print("the result is True")

else:
    print("the result is False")
