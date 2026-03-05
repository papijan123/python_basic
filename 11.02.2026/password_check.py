name="papijan"
password=1234
n=input("input your user name:")
p=int(input("input your password:"))
r=input("input your role:")
if n==name:
	if p==password:
		if r=="admin":
			print("welcome admin")
		elif r=="user":
			print("welcome user")
		else:
			print("cant identify your role")
	else:
		print("incorrot password")
else:
	print("user name is wrong")
	