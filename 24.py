d = {
    "Name": "Milan",
    "Age": 20,
    "City": "Amreli"
}

print("Dictionary =", d)

print("dict() =", dict(d))
print("Length =", len(d))

print("Value of Name =", d.get("Name"))

print("Keys =", d.keys())
print("Values =", d.values())
print("Items =", d.items())

copy_dict = d.copy()
print("Copied Dictionary =", copy_dict)

d.update({"Age": 21})
print("After update =", d)

print("Pop =", d.pop("City"))
print("After pop =", d)

print("Popitem =", d.popitem())
print("After popitem =", d)

d.clear()
print("After clear =", d)