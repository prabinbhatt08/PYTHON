marks = int(input("enter the marks: "))

if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"

print("The grade is: ", grade)



