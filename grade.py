import sys

if len(sys.argv) == 6:
    print("usage:python grade.py <sub1> <sub2> <sub3> <sub4> <sub5>")

     script_name=sys.argv[0]
     sub1=sys.argv[1]
     sub2=sys.argv[2]
     sub3=sys.argv[3]
     sub4=sys.argv[4]
     sub5=sys.argv[5]
print("user marks")
else:
    script_name=sys.argv[0]
     sub1="53"
     sub2="40"
     sub3="90"
     sub4="32"
     sub5="67"
 print("no input given -using default values")
total=sub1+sub2+sub3+sub4+sub5
average=total/5
    
    

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("subject:", sub1)
print("subject:", sub2)
print("subject:", sub3)
print("subject:", sub4)
print("subject:", sub5)
print("total marks:",total)
print("Average Marks:", average)
print("Grade:", grade)


