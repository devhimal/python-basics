# Ask the user to input a number and print its multiplication table from 1 to 10.

inputNumber = int(input("Enter a number to print its multiplication table: "))

if inputNumber < 0:
    print("Please enter a positive number.")
else:
    print(f"Multiplication table for {inputNumber}:\n")
for i in range(1, 11):
    print(f"{inputNumber} x {i} = {inputNumber * i}\n")
    
