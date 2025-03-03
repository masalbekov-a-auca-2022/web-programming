def greet():
    print("Welcome")
greet()

def greet_user(name):
    print("Welcome", name)
greet_user("John")

def greet_def_user(name = "Guest"):
    print("Hello", name)
greet_def_user()
greet_def_user("John")

def add(a,b):
    return a+b

print(add(5, 10))

def rectangle(l, w):
    a = l*w
    p = 2*(l+w)
    return a, p

a, p = rectangle(5, 3)
print(f"Area: {a}, Perimeter: {p}")

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name = "John", age = 30, height = 1.5)

square = lambda x : x*x
print(square(5))

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

def multiply(a,b):
    """This func multiplies two numbers"""

    return a * b

print(multiply.__doc__)

