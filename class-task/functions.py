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
