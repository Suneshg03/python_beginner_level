#FIND THE POWER OF A NUMBER

#METHOD1
value=int(input("ENTER THE VALUE:"))
power=int(input("ENTER THE POWER VALUE:"))
power_of_value=value**power
print(f"The power of value:{power_of_value}")

#METHOD2
value=int(input("ENTER THE VALUE:"))
power=int(input("ENTER THE POWER VALUE:"))
power_of_value=pow(value,power)
print(f"The power of value:{power_of_value}")

#METHOD3
value=int(input("ENTER THE VALUE:"))
power=int(input("ENTER THE POWER VALUE:"))
result=1
while power>0:
    result=result*value
    power=power-1
print(f"The result is:{result}")
