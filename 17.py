l = [10, 20, 30, 40]

print("Original List:", l)

print("Length:", len(l))
print("Count of 20:", l.count(20))
print("Index of 30:", l.index(30))

l.append(50)
print("After append:", l)
l.insert(2, 25)
print("After insert:", l)
l.extend([60, 70])
print("After extend:", l)
l.remove(25)
print("After remove:", l)
x = l.pop()
print("Popped Item:", x)
print("After pop:", l)
l.reverse()
print("After reverse:", l)
copy_list = l.copy()
print("Copied List:", copy_list)
l.sort()
print("After sort:", l)

l.clear()
print("After clear:", l)