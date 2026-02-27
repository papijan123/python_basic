name="papijan"
password=1234
n=input("Input Your User Name:")
p=int(input("Input Your Password:"))
r=input("Input Your Role:")
if n==name and p==password:	
		if r=="admin":
			print("Welcome Admin")
		elif r=="user":
			print("Welcome User")
		else:
			print("Cant Identify Your Role")
else:     
    print("User Name Or Password Is Incorrot")