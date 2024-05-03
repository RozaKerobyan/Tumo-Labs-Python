data = {"John":2500,"Julie":3500,"Anna":1800}

print("--------")

print(data["Anna"])

data2 = {
    "boys":["Arman","Hakob","Tigran","Artash"],
    "girls":["Flora","Tatev","Hasmik","Narine"]
}

print("--------")

print(data2)

print("--------")

print(data2["boys"])

print("--------")

print("--------")

# print(data["John"])

print(data.get("Arman"))

print("--------")

data["Anna"] = 500
print(data)

print("--------")

data2["girls"].append("Varsenik")
print(data2["girls"])

print("--------")

data.update({"Anna":200,"Julie":100})
print(data)

print("--------")

print(data2.keys())
print(data2.values())


