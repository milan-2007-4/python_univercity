lst = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

result = [x for i, x in enumerate(lst) if i not in (0, 2, 3, 5)]

print("Original List:", lst)
print("New List:", result)