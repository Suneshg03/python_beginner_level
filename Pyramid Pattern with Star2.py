 #        *
 #      *   *
 #    *   *   *
 #  *   *   *   *
 # *   *   *   *   *

num=int(input("Enter the count:"))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")
    print()