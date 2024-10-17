#FUNCTION THAT TAKES A SEQUENCE OF NUMBERS AND DETERMINES WHETHER ALL ARE DIFFERENT FROM EACH OTHER:

#METHOD 1:USING FUNCTION
def test(data):

    if len(data)==len(set(data)):
        return True

    else:
        return False


print(test([1,5,7,9]))

print(test([2,4,5,5,7,9]))





#METHOD 2:WITHOUT USING FUNCION

data1=[1,5,7,9]
if len(data1)==len(set(data)):
    print(True)

else:
    print(False)


