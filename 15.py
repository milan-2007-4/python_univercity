# Program 15

file = open("sample.txt", "r")

text = file.read()

file.close()

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Characters =", characters)
print("Words =", words)
print("Lines =", lines)