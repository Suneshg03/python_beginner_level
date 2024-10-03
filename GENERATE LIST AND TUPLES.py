#GENERATE A LIST AND TUPLE WITH COMMA-SEPARATED NUMBER:
#METHOD 1
numbers=int(input("ENTER THE RANGE OF VALUE:"))
values=[]
for i in range(numbers):
    value=int(input("ENTER THE NUMBER:"))
    values.append(value)
print(values)
con_tuple=(tuple(values))
print(con_tuple)  


#METHOD 2
values=input("ENTER THE VALUES:")
lst=values.split(",")
tuple1=tuple(lst)
print("list:",lst)
print("tuple:",tuple1)
