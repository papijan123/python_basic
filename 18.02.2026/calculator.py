n1=int(input("input a number:"))
n2=int(input("input a number:"))
print("(+)=1","\n","(-)=2","\n","(*)=3","\n","(/)=4")  
c=int(input(":"))
if c>0 and c<=4:
    if c==1:
        print("final answer:",n1+n2)
    elif c==2:
        print("final answer:",n1-n2)
    elif c==3:
        print("final answer:",n1*n2)
    else:
        if n2!=0:
            print("final answer:",n1/n2)
        else:
            print("can't divide a number by 0")
else:
    print("input a valid number")