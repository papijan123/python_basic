s=int(input("Input your salary:"))
t=0
n=0
if s>=100000:
    t=s*(0.05)
elif s>=80000:
    t=s*(0.03)
n=s-t
print("basic salary""\t:",s,"\n","net salary""\t:",n,"\n","tax:",t)
