# Create a list of keys for a dictionary
key = ["name", "age", "city", "email", "address", "phone"]
# Create a list of values that correspond to the keys
value = ["Himal Tamang", 12, "Kathmandu", "himal@gmail.com",9818283722]
# Print the key and value lists
print(key, value)

# Iterate over the key and value lists simultaneously
for i, j in zip(key, value):
    # Print the key-value pairs
    print(f"{i}: {j}")


# Iterate over the key and value lists with an index
for i, (j, k) in enumerate(zip(key, value)):
    # Print the index and the key-value pair
    print(f"{i}: {j} - {k}")

 # Dictionary Comprehension
# Create a dictionary with numbers as keys and their squares as values
square = {i: i**2  for i in range(1, 11)}
# Print the dictionary of squares
print(square)


# Sets
# Create a set of numbers
elements = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Print the set
print("Set:", elements)
# Print the length of the set
print("Set Length:", len(elements))
# Print the type of the data structure
print("Set Type:", type(elements))
# Add an element to the set
elements.add(11)
# Remove an element from the set
elements.remove(1)
# Discard an element from the set (does not raise an error if the element is not found)
elements.discard(2)
# Remove and return an arbitrary element from the set
elements.pop()
# Print the updated set
print("Updated Set:", elements)


# Create a set of numbers
set1 = {1, 2, 3, 4, 5}
# Create another set of numbers
set2 = {4, 5, 6, 7, 8}


# Print the first set
print("Set 1:", set1)
# Print the second set
print("Set 2:", set2)

# Find the union of the two sets
union_set = set1.union(set2)
# Find the union of the two sets using the | operator
union_set2 = set2 | set1
# Find the intersection of the two sets
intersect_set = set1.intersection(set2)
# Find the difference between the two sets (elements in set1 but not in set2)
difference_set = set1.difference(set2)
# Find the difference between the two sets (elements in set2 but not in set1)
difference_set2 = set2.difference(set1)
# Find the symmetric difference between the two sets (elements in either set, but not both)
symmetric_difference_set = set1.symmetric_difference(set2)
# Print the union of the two sets
print("Union:", union_set)
# Print the union of the two sets
print("union_set2", union_set2)
# Print the intersection of the two sets
print("Intersection:", intersect_set)
# Print the difference between the two sets
print("Difference:", difference_set)
# Print the difference between the two sets
print("Difference 2:", difference_set2)


# Print even numbers from 0 to 100 
even_numbers = [i for i in range(100) if i % 2 == 0]
print("Even numbers from 0 to 100:", even_numbers)
