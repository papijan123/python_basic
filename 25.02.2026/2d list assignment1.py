m=[[90,88,65],[83,73,63],[93,73,86]]
s=["kabil","anusa","vimal"]
print(f"s.name     maths   science ict     total   avarage   rank")
print("----------------------------------------------------------")
z=0
while z<3:
    t=m[z][0]+m[z][1]+m[z][2]
    avg=t/3
    if avg>=75:
        rank="A"
    elif avg>=65:
        rank="B"
    elif avg>=55:
        rank="c"
    else:
        rank="s"
    print(s[z],"    ",m[z][0],"    ",m[z][1],"    ",m[z][2],"    ",(t),"    ",(avg),"   ",(rank))
    print("----------------------------------------------------------")
    z+=1
