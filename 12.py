# Program 12

source = open("sample.txt", "r")
destination = open("copy.txt", "w")

destination.write(source.read())

source.close()
destination.close()

print("File Copied Successfully")