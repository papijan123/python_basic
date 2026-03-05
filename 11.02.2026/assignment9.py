n=int(input("input a number:"))
y=n%2
if n>=0:
    if y==1:
        print("odd number")
    else:
        print("even number")
else:
    print("input a positive number")
