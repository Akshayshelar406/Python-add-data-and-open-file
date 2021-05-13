# Original code, f.close() must be called manualy.
# f=open("one.txt","r")
# print(f.read(10))


# New code, f.close() is called automaticaly.
with open("one.txt", "r") as f:
    # file name variable is "f"
    file_contents = f.read() # Reads the file and stores contents in "file_contents" variable.
    print(file_contents) # Prints file contents.
    # No need to close file, since file was opened using the "with" context manager. In other words, "with" closes the file automaticaly
