def calculate(a, b):
    s = a + b
    d = a - b
    p = a * b
    return s, d, p

sum1, diff, prod = calculate(10, 5)

print("Sum =", sum1)
print("Difference =", diff)
print("Product =", prod)