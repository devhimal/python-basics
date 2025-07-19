# Write a program to count how many vowels are in a string entered by the user.

inputString = input("Enter a string to count the vowels: ")
vowels = "aeiouAEIOU"
count = 0

if not inputString:
    print("Please enter a non-empty string.")
else:
    for char in inputString:
        if char in vowels:
            count += 1


print(f"The number of vowels in the string is: {count}")
