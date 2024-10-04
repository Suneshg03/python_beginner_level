#CHECK WHETHER A SPECIFIED VALUE IS CONTAINED IN A GROUP OF VALUES
#METHOD 1:USING FIXED VALUE

list_value=[4,5,6,7]
specific_value=int(input("ENTER SPECIFIC VALUE CONTAINED IN A LIST:"))
if specific_value in list_value:
    print(True)

else:
    print(False)


#METHOD 2:USING USER INPUT

n=int(input("ENTER THE RANGE:"))
list_value=[]
specific_value=int(input("ENTER SPECIFIC VALUE CONTAINED IN A LIST:"))
for i in range(n):
    values=int(input("ENTER THE LIST VALUES:"))
    list_value.append(values)
if specific_value in list_value:
    print(True)

else:
    print(False)


#METHOD 3:USING FUNCTION

def is_group_member(group_data,n):
    for value in group_data:
        if n==value:
            return True

    return False
print(is_group_member(group_data=[1,2,3],n=3))
print(is_group_member(group_data=[1,2,3,4,5,7],n=-1))
