x = 100      # Global Variable

def demo():
    y = 50   # Local Variable
    print("Inside Function")
    print("Global Variable =", x)
    print("Local Variable =", y)

demo()

print("Outside Function")
print("Global Variable =", x)