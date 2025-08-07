# method 1
file = open("./himal.txt")
print(file.read())


# method 2
with open("./himal.txt") as file:
    print(file.read())

# Writing to a file
with open("./himal.txt", "w") as file:
    file.write("This is a new line added to the file.\n")

with open("./himal.txt") as f:
    print(f.read())


# Creating a new file

import os
if os.path.exists("./new_file.txt"):
    os.remove("./new_file.txt")
else:
    print("The file does not exist")


# Now, working with json files

import  json

x = {"name": "John", "age": 30, "city": "New York"}

with open('./data.txt', "w") as file:
    json.dump(x, file)

# Copying one file from source to destination

def copy_file(source, destination):
    with open(source, "rb") as src:
        with open(destination, "wb") as dst:
            dst.write(src.read())
    print(f"File Copied from {source} to {destination}")

copy_file("../README.md", "./himal.txt")
