d = {'A': 30, 'B': 10, 'C': 20}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("Original Dictionary:", d)
print("Ascending:", asc)
print("Descending:", desc)