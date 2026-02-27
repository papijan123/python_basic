def PrintStudentName(name):
    print("student name is:",name)
num=int(input("enter student total number:"))
for x in range(num):
    name=input("enter student name:")
    PrintStudentName(name)