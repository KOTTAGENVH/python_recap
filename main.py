from typing import Final
from abc import ABC, abstractmethod

#Youtube Link: https://www.youtube.com/watch?v=Gx5qb1uHss4
#Variables with types
number: int = 10
name: str = "John"
decimal: float = 10.5
active: bool = True

#Lists
numbers: list[int] = [1, 2, 3, 4, 5] #Stores all atribary value of elements.
#Tuples
numbers: tuple[int, str] = (1, "John") #A lot like list but are immutable.
#Set
numbers: set[int] = {1, 2, 3, 4, 5} #No duplicates all are unique.
#Dictionaries
numbers: dict[str, int] = {"one": 1, "two": 2, "three": 3} #Key value pairs.

#Loops
for i in numbers:
    print(i) #Prints all elements in the list.

while number > 0:
    print(number) #Prints the number until it is 0.
    number -= 1 #Decreases the number by 1.

#Constants
VERSION: Final[str] = "1.0.0" #Final is used to define a constant variable.

#Functions
def add(a: int, b: int) -> int: #If you dont return anything None type can be used for return can be removed.
    return a + b #Adds two numbers and returns the result.
def greet(name: str) -> str:
    return f"Hello, {name}!" #Greets the user with the name provided.

greet("John") #Calls the greet function with the name "John".
add(1, 2) #Calls the add function with the numbers 1 and 2.

#Classes
class Person:
    def __init__(self, name: str, age: int): #Initializer used to set an instance of the class.
        self.name = name
        self.age = age

    #Dunder methods: __str__, __repr__, __eq__, __lt__, __le__, __gt__, __ge__ 
    # Dunder methods are used to define the behavior of the class when it is used in a certain way.

    def __str__(self) -> str: #Used to define the string representation of the class. Comment this to see the use of the dunder method.
        return f"Person(name={self.name}, age={self.age})"
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("John", 30) #Creates an instance of the Person class.
print(person) #Prints the string representation of the Person class.
print(person.greet()) #Calls the greet method of the Person class.

#OOP Concepts
#Encapsulation: 
# Hiding the internal state of the object and requiring all interaction to be performed through an object's methods.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

#Inheritance:
# A way to form new classes using classes that have already been defined.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

pet = Dog()
pet.speak()  # Dog barks

#Polymorphism:
def animal_sound(animal):
    animal.speak()

animal_sound(Dog())  # Dog barks
animal_sound(Animal())  # Animal speaks

#Abstraction:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
