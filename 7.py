# Program 7

num = int(input("Enter Number: "))

if num > 0:
    print("Positive Number")

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

marks = int(input("Enter Marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")