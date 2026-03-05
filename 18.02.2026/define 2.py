n1=int(input("input n1:"))
n2=int(input("input n2:"))
c=int(input(":"))
if c>=1 and c<=4:
    def printfinal(num1,num2):
        if c==1:
            return n1+n2
        elif c==2:
            return n1-n2
        elif c==3:
            return n1*n2
        elif n2>0:
            return n1/n2
        else:
            print("can't define the number")
else:
    print("input a valid number:")
final=printfinal(n1,n2)
print(final)
