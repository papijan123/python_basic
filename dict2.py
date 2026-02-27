d=[("name","seelan"),("age",39),("gender","male")]
data=dict(d)
print(data)
print(type(d))
print(data["name"])
print(data["age"])
print(data["gender"])
data.get("name")
data["nic"]=1087497489
print(data["nic"])
data.update({"age":40,"nic":6785656})
print(data)
data.get("dob","2002/02/24")
data.get("city")
print(data)
del data["name"]
print(data)
data.pop("age")
print(data)
data.popitem()
print(data)
data.clear()
print(data)


