#INPUT AN INTEGER(n) AND COMPUTES THE VALUES OF n+nn+nnn

#METHOD 1
num=int(input("ENTER THE NUMBER:"))
num_times=int(input("ENTER NUMBER OF TIME:"))
times=[]
for i in range(1,num_times+1):
    term=int(str(num)*i)
    times.append(term)
con_times=sum(times)

print(f"the result of n + nn + nnn is:{con_times}")

#METHOD 2
num=int(input("ENTER THE NUMBER:"))
n1=int("%s"%num)
n2=int("%s%s"%(num,num))
n3=int("%s%s%s"%(num,num,num))
print(n1+n2+n3)


#METHOD 3
number=int(input())
count=""
count1=0
for i in range(1,4):
    b=i*str(number)
    count=count+b+"+"
    count1=count1+int(b)
print(count)
print(count1)
