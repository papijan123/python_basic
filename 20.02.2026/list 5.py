months=["Jau","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
salary=[30000,35000,40000,50000,58000,83000,88000,100000,150000,19000,25000,300000]
ts=0
tt=0
tn=0
x=0
print(f"month      basic        tax          net")
while x<12:
    if salary[x]<=50000:
        tax=salary[x]*(0.03)
    elif salary[x]<=100000:
        tax=(salary[x]-50000)*(0.05)+(50000*0.03)
    elif salary[x]<=300000:
        tax=(50000*0.03)+(50000*0.05)+((salary[x]-100000)*0.08)
    elif salary[x]>300000: 
        tax=(50000*0.03)+(50000*0.05)+(200000*0.08)+((salary[x]-300000)*0.1)
    net=salary[x]-tax
    print(f"{months[x]}        {salary[x]}        {tax}        {net}")
    ts+=salary[x]
    tt+=tax
    tn+=net
    x+=1

print("---------------------------------------------------")
print(f"           {ts}        {tt}     {tn}")         
    