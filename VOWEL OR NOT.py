#VOWELS OR NOT
#METHOD 1: CHARACTER IS VOWEL OR NOT

a=input("ENTER ANY ALPHABET LETTER:")
vowels="aeouiAEOUI"
if a in vowels:
    print(a,"IS A VOWEL")

else:
    print(a,"IS NOT A VOWEL")



#METHOD 2: WORD IS VOWEL OR NOT
a=input("ENTER ANY CHARACTERS:")
vowels="aeouiAEOUI"
for i in a:
    if i in vowels:
        print(i,"VOWEL")

    else:
        print(i,"NOT VOWELS")


#METHOD 3
a=input("ENTER YOUR CHARACTER:")
if (a=="a" or a=="e" or a=="o" or a=="u" or a=="i"):
    print(a,"is vowel")

elif (a=="A" or a=="E" or a=="O" or a=="U" or a=="I"):
    print(a,"is vowel")

else:
    print(a,"is consonant")
