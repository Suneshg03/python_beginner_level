#CONCATENATE ALL ELEMENTS IN A LIST INTO A STRING
#METHOD 1:USING FIXED VALUE

lst=[1,2,3,4,5]
count=""
for i in lst:
    count=count+str(i)
print(count)


#METHOD 2:USING FUNCTION


def concatenate_list_data(lst):
    result=""
    for element in lst:
        result=result+str(element)

    return result

print(concatenate_list_data([1,5,12,2]))
