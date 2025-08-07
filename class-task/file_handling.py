# method 1
file = open("./himal.txt")
print(file.read())


# method 2
with open("./himal.txt") as file:
    print(file.read()) 
