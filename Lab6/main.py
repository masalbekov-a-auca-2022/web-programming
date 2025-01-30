a = int(input("int: "))
b = float(input("float: "))
c = input("string: ")

print(type(a), type(b), type(c))

print(type(int(c)),type(float(c)))

person = {
    "name": "Aziret",
    "age": 19
}

print(person.get("name"), person.get("age"))

x = {1, 2, 3}

x.add(5)
x.remove(2)

print(2 in x)
print(5 in x)