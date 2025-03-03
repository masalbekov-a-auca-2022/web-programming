try:
    x = int(input("Enter a number: "))
    print(10/x)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Please enter a valid number")

#multiple exceptions

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ZeroDivisionError, ValueError):
    print("Invalid operation")

#else

try:
    x = int(input("Enter a number: "))
    res = print(10/x)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Please enter a valid number")
else:
    print(res)

#finally
try:
    file = open("file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    file.close()

#rasing

def withdraw(a, b):
    if a > b:
        raise ValueError("Error")
    return b - a

try:
    new_b = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")



