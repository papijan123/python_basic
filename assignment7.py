m=int(input("input your marks:"))
if m<=100 and m>=0:
    if m>=75:
        print("A")
    elif m>=65:
        print("B")
    elif m>=55:
        print("C")
    elif m>=40:
        print("S")
    else:
        print("F")
else:
    print("Input a valid value")
    
    
