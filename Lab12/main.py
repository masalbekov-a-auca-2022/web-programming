from math import acosh


class Car:
    def __init__(self, brand, speed, color):
        self.brand = brand
        self.speed = speed
        self.color = color

    def display_info(self):
            return f"{self.color} {self.brand} {self.speed}"

car = Car("Toyota", 45, "Orange")
print(car.display_info())

class Dog:

    owner = "Tyler"

    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Alex")
print(dog.bark())

dog.name = "Hunter"
print(dog.bark())

dog2 = Dog("Ben")

print(dog2.owner)
print(dog.owner)

Dog.owner = "Melissa"

print(dog2.owner)
print(dog.owner)

class User:
    def __init__(self, username, password):

        self.username = username
        self.__password = password
    def login(self, password):
        if password == self.__password:
            return True
        else:
            return False

user = User("admin", "123")

print(user.login("123"))
print(user.login("123411"))

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print( f"successfully deposited {amount}, new __balance is {self.__balance}")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"successfully withdrawn {amount}, new __balance is {self.__balance}")
        else:
            print("error")
    def get___balance(self):
        return self.__balance

account = BankAccount("Tyler", 1000)
account.deposit(500)
account.withdraw(100)

print(account.get___balance())
#print(account.__balance)

class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return ("sound")

class Dog(Animal):
    def make_sound(self):
        return ("WOOF!")
class Cat(Animal):
    def make_sound(self):
        return ("MEOW!")

dog = Dog("Hunter")
cat = Cat("Ben")
print(dog.make_sound())
print(cat.make_sound())


class Bird:
    def fly(self):
        return "bird fly using nature force"
class Airplane:
    def fly(self):
        return "airplane fly using magic"
class Fish:
    def fly(self):
        return "fish can't fly because they don't have a soul"
for obj in [Bird(), Airplane(), Fish()]:
    print(obj.fly())

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car_A(Vehicle):
    def start_engine(self):
        print("Car start engine")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike start engine")

#car = Vehicle()

carA = Car_A()
bike = Bike()

carA.start_engine()
bike.start_engine()