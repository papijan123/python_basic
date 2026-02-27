n1=int(input("input a number:"))
n2=int(input("input a number:"))
print("(+)=1","\n","(-)=2","\n","(*)=3","\n","(/)=4")
c=int(input(":"))
match c:
    case 1:
        print("final answer:",n1+n2)
    case 2:
        print("final answer:",n1-n2)
    case 3:
        print("final answer:",n1*n2)
    case 4:
        print("final answer:",n1/n2)
    case _:
        print("input a valid number")