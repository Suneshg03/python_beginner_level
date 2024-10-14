# MAXIMUM - MINIMUM NUMBERS FROM A LIST:

lst=[23,4,1,44,0,34,-2,55]
min_lst=lst[0]
max_lst=lst[0]
for i in lst:
    if i>min_lst:
        max_lst=i
    else:
        min_lst=i
print("The maximum number is:",max_lst)
print("The minimum number is:",min_lst)
