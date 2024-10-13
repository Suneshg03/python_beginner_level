#CALCULATE THE SUM OF ALL ITEMS OF A SET AND DICTIONARY

#METHOD 1:BY SET
set_value={100,200,300,400}
count=0
for i in set_value:
    count=count+i
print("the sum is:",count)


#METHOD 2:BY DICTIONARY
dict1={"a":100,"b":200,"c":300,"d":400}
count=0
for i in dict1.values():
    count=count+i
print("the sum is:",count)
