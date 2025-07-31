def person_name(name):
    return name;


# calling the function
person = person_name("Himal Tamang.")
print(person)

# Printing the fibonacci series
def fibonacci(n):
    print("Fibonacci series:")
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()

# Calling the function
fibonacci(100)

# lambda arguments: expression
# Regular function
def square(x):
    return x * x
print("Square of 5 using regular function:", square(5))

# Lambda function
square_lambda = lambda x: x * x
print("Square of 5 using lambda function:", square_lambda(5))


# Nested function, printing multiplication table using nested function.
def times(x):
    def multiplier(y):
        return x * y
    return multiplier

multiply_by = times(7)

for i in range(1, 11):
    result= multiply_by(i)
    print(f"{7} x {i} = {result}")


# *ags and *kwargs in python, variable length arguments

def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="Alice", age=30)

# Create a dictionary and write a function to search a valueusing key and return the specific value.


students = {
    1: {"name": "Alice", "age": 20, "grade": "A"},
    2: {"name": "Bob", "age": 21, "grade": "B"},
    3: {"name": "Charlie", "age": 22, "grade": "A"},
    4: {"name": "David", "age": 20, "grade": "C"},
    5: {"name": "Eve", "age": 23, "grade": "B"},
    6: {"name": "Frank", "age": 19, "grade": "A"},
    7: {"name": "Grace", "age": 22, "grade": "B"},
    8: {"name": "Heidi", "age": 21, "grade": "C"},
    9: {"name": "Ivan", "age": 20, "grade": "B"},
    10: {"name": "Judy", "age": 23, "grade": "A"}
}

# Example: print details of student with ID 3
print(students[3])

def find_student_by_id(student_id):
    if student_id in students:
        return students[student_id]
    else:
        return "Student not found."

finded_student = find_student_by_id(10)

print(f"Name of student with ID 10 Name: {finded_student['name']}")
print(f"Name of student with ID 10 Age: {finded_student['age']}")
print(f"Name of student with ID 10 Grade: {finded_student['grade']}")
print(f"Details of student with ID 11: {find_student_by_id(11)}") # This will return "Student not found."



#Function Decorators, this allow us to modify and extend the behaviour  of functions without changing the code.


import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def example_function():
    time.sleep(2)
    print("Function executed.")

example_function()

