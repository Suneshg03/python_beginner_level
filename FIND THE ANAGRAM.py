#ANAGRAM
#METHOD 1:USING STRINGS
word1=input("ENTER FIRST WORD:").upper()
word2=input("ENTER SECOND WORD:").upper()
str1=sorted(word1)
str2=sorted(word2)
print("word1=",str1)
print("word2=",str2)
if len(word1)==len(word2):
    if str1==str2:
        print("its anagram")

    else:
        print("its not anagram")

else:
    print("its not anagram")



#METHOD 2:USING INTEGERS

num1=int(input("ENTER FIRST NUMBERS:"))
num2=int(input("ENTER SECOND NUMBERS:"))
convert=str(num1)
convert1=str(num2)
int1=sorted(convert)
int2=sorted(convert1)
print("num1=",int1)
print("num2=",int2)
if int1==int2:
        print("its anagram")

else:
     print("its not anagram")


