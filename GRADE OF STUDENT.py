#THE GRADE OF STUDENT
#METHOD 1:USING FIXED NUMBER OF SUBJECTS

student_id=input("ENTER STUDENT ID:")
student_name=input("ENTER STUDENT NAME:")
subject1=int(input("ENTER SUBJECT1 MARK:"))
subject2=int(input("ENTER SUBJECT2 MARK:"))
subject3=int(input("ENTER SUBJECT3 MARK:"))
total_mark=subject1+subject2+subject3
average=total_mark/3
print(format(average,".2f"))

if average>=90 and average<=99:
    print("the grade is:A+")

elif average>=80 and average<=89:
    print("the grade is:A")

elif average>=70 and average<=79:
    print("the grade is:B+")

elif average>=60 and average <=69:
    print("the grade is:B")

elif average>=50 and average<=59:
    print("the grade is:C+")

else:
    print("the grade is is:E")



#METHOD 2: USING NUMBER OF SUBJECTS
    
stu_id=input("ENTER STUDENT ID:")
stu_name=input("ENTER STUDENT NAME:")
num=int(input("ENTER NUMBER OF SUBJECT:"))
subjects=[]
for i in range(0,num):
    count_sub=int(input("ENTER SUBJECT MARKS:"))
    subjects.append(count_sub)
average=sum(subjects)/num

print(format(average,".2f"))
if average>=90 and average<=99:
      print("the grade is:A+")

elif average>=80 and average<=89:
    print("the grade is:A")

elif average>=70 and average<=79:
    print("the grade is:B+")

elif average>=60 and average<=69:
    print("the grade is:B")

elif average>=50 and average<=59:
    print("the grade is:C+")

else:
    print("the grade is:E")
