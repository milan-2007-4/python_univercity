s1 = {10, 20, 30}
s2 = {30, 40, 50}

print("Set1 =", s1)
print("Set2 =", s2)

s1.add(60)
print("After add():", s1)

s1.update([70, 80])
print("After update():", s1)

s1.remove(20)
print("After remove():", s1)

x = s1.pop()
print("Popped Item:", x)
print("After pop():", s1)

s1.discard(100)
print("After discard(100):", s1)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

s1.clear()
print("After clear():", s1)