def PrintStudentDetails(name,age,grade):
	print(f"student name is:{name},student age is:{age},student grade is:{grade}")
num=int(input("enter the total students:"))
for x in range(num):
        name=input("enter the studen name:")
        age=int(input("enter the student age:"))
        grade=int(input("enter the student grade:"))
        PrintStudentDetails(name,age,grade)