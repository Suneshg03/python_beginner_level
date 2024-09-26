#FIND THE POWER OF LAST NUMBER
num=int(input("ENTER A NUMBER:"))
power_num=int(input("POWER NUMBER:"))
power=num**power_num
print(power)
print(f"the last number is {power%10}")
