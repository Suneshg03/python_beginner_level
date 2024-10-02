# FIND THE NUMBER OF OCCURRENCES OF A SUBSTRING IN A STRING:

#METHOD 1: BASIC USER INPUTS METHOD

str1=input("ENTER THE STRING:")
str2=input("ENTER THE SUBSTRING:")
count=str1.count(str2)
print(f"{str2} is {count} occur")


#METHOD 2: USING FUNCTION

def count_emma(str_x):
    print("Given string:",str_x)
    count=0
    for i in range(len(str_x)-1):
        count+=str_x[i:i+4]=='Emma'
    return count
count=count_emma("Emma is a good developer. Emma is a good writer")
print("Emma appeared",count,'times')


#METHOD 3:USING SPLIT() FUNCTION
str1=input("ENTER THE STRING::")
b=str1.split()
str2=input("ENTER THE SUBSTRING:")
count=0
for i in b:
    if i==str2:
        count=count+1

print(f"{str2} is {count} occur" )
