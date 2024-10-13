#SORTING THREE INTEGERS
#METHOD 1:SORT THREE INTEGERS WITHOUT USING CONDITIONAL STATEMENT AND LOOPS
n1=int(input("ENTER FIRST NUMBER:"))
n2=int(input("ENTER SECOND NUMBER:"))
n3=int(input("ENTER THIRD NUMBER:"))

minimum=min(n1,n2,n3)

maximum=max(n1,n2,n3)

middle=(n1+n2+n3)-minimum-maximum

print("Numbers in sorted order:",minimum,middle,maximum)


#METHOD 2:USING CONDITIONAL STATEMENTS

a, b, c = input("ENTER THE NUMBGERS:").split()
a = int (a)
b = int (b)
c = int (c)

if a < b and a < c:
   smallest = a
elif b < a and b < c:
   smallest = b
else:
   smallest = c

if a > b and a < c:
   middle = a
elif a < b and a > c:
   middle = a
elif b > a and b < c:
   middle = b
elif b < a and b > c:
   middle = b
else:
   middle = c


if a > b and a > c:
   largest = a
elif b > a and b > c:
   largest = b
else:
   largest = c

print("Numbers in sorted order:",smallest, middle, largest)
