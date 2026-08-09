# Different ways of creating dictionary objects

# Method 1
d1 = {"Name": "Milan", "Age": 20}
print("Dictionary1 =", d1)

# Method 2
d2 = dict(Name="Rahul", Age=21)
print("Dictionary2 =", d2)

# Method 3
d3 = dict([("A", 1), ("B", 2)])
print("Dictionary3 =", d3)

# Method 4
d4 = {}
d4["City"] = "Rajkot"
d4["State"] = "Gujarat"
print("Dictionary4 =", d4)

# Method 5
d5 = {x: x*x for x in range(1, 6)}
print("Dictionary5 =", d5)