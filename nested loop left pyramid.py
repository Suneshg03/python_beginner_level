#nested loop left pyramid

n=5
for i in range(n):
    for j in range(1,i+1):
        print("*",end="")
    print()
for k in range(n,0,-1):
    for L in range(1,k+1):
        print("*",end="")

    print()



n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*",end="")

    print()


