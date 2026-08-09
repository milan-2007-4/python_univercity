# Program 5: Operators

a = 15
b = 4

print("Arithmetic Operators")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

print("\nRelational Operators")
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

print("\nAssignment Operator")
c = a
c += 5
print(c)

print("\nLogical Operators")
print(a>10 and b<5)
print(a<10 or b<5)
print(not(a>b))

print("\nBitwise Operators")
print(a & b)
print(a | b)
print(a ^ b)

print("\nTernary Operator")
largest = a if a>b else b
print("Largest =", largest)