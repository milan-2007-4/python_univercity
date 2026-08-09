# Different ways of creating set objects

# Method 1
s1 = {10, 20, 30}
print("Set1 =", s1)

# Method 2
s2 = set([40, 50, 60])
print("Set2 =", s2)

# Method 3
s3 = set("Python")
print("Set3 =", s3)

# Method 4
s4 = set()
s4.add(70)
s4.add(80)
print("Set4 =", s4)

# Method 5
s5 = {x for x in range(1, 6)}
print("Set5 =", s5)