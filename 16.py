# Different ways of creating list objects

# Method 1
list1 = [10, 20, 30]
print("List1 =", list1)

# Method 2
list2 = list((40, 50, 60))
print("List2 =", list2)

# Method 3
list3 = list("Python")
print("List3 =", list3)

# Method 4
list4 = []
list4.append(70)
list4.append(80)
print("List4 =", list4)

# Method 5
list5 = [x for x in range(1, 6)]
print("List5 =", list5)