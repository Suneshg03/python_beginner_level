#SUM OF NATURAL NUMBERS WITH RECURSION
def recursion(num):
    if num==0 or num==1:
        return 1

    else:
        return num+recursion(num-1)

num=int(input("ENTER A NUMBER:"))
print("the sum is",recursion(num))
