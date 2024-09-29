#SUM OF NATURAL NUMBERS WITH RECURSION
def recursion(a):
    if a==0 or a==1:
        return 1

    else:
        return a+recursion(a-1)

num=int(input("ENTER A NUMBER:"))
print("the sum is",recursion(num))
