# Program 13

file = open("sample.txt", "r")

text = file.read()

file.close()

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)