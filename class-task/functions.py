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


