n=int(input("input a number:"))
if n>0 and n<=7:
	if n==1:
		print("monday")
	elif n==2:
		print("tuesday")
	elif n==3:
		print("wednsday")
	elif n==4:
		print("thursday")
	elif n==5:
		print("friday")
	elif n==6:
		print("saterday")
	else:
		print("sunday")
else:
	print("input a valid number")
	