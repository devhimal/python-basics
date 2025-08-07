numbers = [3, 4, 5, 6, 7, 8, 10]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
print(f"The maximum number in the list is :{max_num}")
