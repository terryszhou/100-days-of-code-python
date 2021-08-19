# METHOD 1: DIRECT VARIABLE
# file = open("24/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# METHOD 2: 'WITH' KEYWORD
# with open("24/my_file.txt", mode="a") as file: # <-- default mode for open() is "r" for "read"
#     file.write("\nNew text.")

# with open("24/new_file.txt", mode="w") as file:
#     file.write("New file.")

with open("24/README.md", mode="w") as file:
    file.write("Test file.")