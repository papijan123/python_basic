u=int(input("input your units:"))
t=0
if u<=90:
	t=u*7
elif u<=150:
	t=(90*7)+((u-90)*10)
elif u<=300:
    t=(90*7)+(60*10)+((u-150)*15)
else:
    t=t=(90*7)+(60*10)+((u-150)*15)+(((u-300)*15)*0.03)
print("total charge:",t)
    