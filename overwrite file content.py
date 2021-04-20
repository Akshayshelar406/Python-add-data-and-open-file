files = open("one.txt", "w")

files.write("This will override all content...")

files.close()

files = open("one.txt", "r")

print(files.read())