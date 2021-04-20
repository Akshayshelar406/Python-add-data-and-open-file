f = open("one.txt", "a")

f.write("This is new line... in file...")

f.close()

f = open("one.txt", "r")

print(f.read())