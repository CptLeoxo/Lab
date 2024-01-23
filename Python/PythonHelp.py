import math
import time
import random
import os
import shutil

"""

# String functions

name = "kaTe"

print(len(name))                    # Delka stringu -> 4
print(name.find("e"))               # Vrati index nalezeneho elementu -> 3
print(name.capitalize())            # Slovo s velkym pismenem -> Kate
print(name.lower())                 # Cely string malymi pismeny -> kate
print(name.upper())                 # Cely string velkymi pismeny -> KATE
print(name.isdigit())               # Bool jestli je string z cisel -> False
print(name.isalpha())               # Bool jestli string je z pismen (mezernik se nepocita jako pismeno -> False) -> True
print(name.count("k"))              # Pocet vyhledanych elementu -> 1
print(name.replace("a", "o"))       # Vymena elementu "x" na "y" -> koTe
print(name*2)                       # Var name se vypise *x -> kaTekaTe

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Data types in python

x = 1           # Int
y = 2.0         # Float
z = "3"         # Str

print(int(y))   # Element jako Int
print(str(x))   # Element jako Str
print(float(x)) # Elemetn jako Float

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Input operator 

name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Hello {name}! Next year you will be {age + 1} year old")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Math library for python

pi = -3.14
x = 1
y = 2
z = 3

print(round(pi))        # Round the number
print(math.ceil(pi))    # Round the number up
print(math.floor(pi))   # Round the number down
print(abs(pi))          # The absolute number from the variable
print(pow(pi,2))        # Power function
print(math.sqrt(420))   # Square root function
print(max(x,y,z))       # The largest value
print(min(x,y,z))       # The smallest value

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Slicing the string

name = "Captain Leo"

first_name = name[:7]       # Slice from 0 to 7 (7 is not icluded)
last_name = name[8:]        # Slice from 8 to the end
funky_name = name[::3]      # Slice all the string by 3
reversed_name = name[::-1]  # Slice all the string by -1
print(first_name, last_name, funky_name, reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
sliced = slice(7, -4)       # Setting the slice start and end
print(website1[sliced], website2[sliced])

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# If statements (if, elif, else)

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You're an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You're a child!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Logical operators (and, or, not)

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
   print("The temperature is good today!\nGo outside!")
elif temp < 0 or temp > 30:
   print("The temperature is bad today!\nStay at home!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# While loop (While loop = unlimited)

name = ""

while len(name) == 0:
    name = input("What is your name?: ")
    
print(f"Hello {name}!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# For loop (For loop = limited)

for i in range(10):
    print(i+1)

for i in range(50,101,2):
    print(i)

for i in "Captain Leo":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nested loops = loop in the loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("With which symbol?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Loop control statements // Break, continue, pass

# Break =       used to termonate the loop entirely
# Continue =    skips to the next itereation of the loop
# Pass =        does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
        
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# List

food = ["pizza", "hotdog", "sushi", "cheese", "steak", "soup"]
print(food)
food[1] = "burger"
print(food)
print(food[1])          # Python starting indexing from 0

food.append("tacos")    # Adding a new element
food.pop()              # Removing the last element
food.remove("cheese")   # Removing the element by its value
food.remove(food[0])    # Removing the element by its index
food.insert(0,"cake")   # Adding the element for a index and value
food.sort()             # Sorting the list
food.clear()            # Deleting all the values from the list


for x in food:
    print(x)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2D lists

drinks = ["cola", "coffee", "soda"]
dinner = ["pizza", "burger", "hotdog"]
desert = ["icecream", "cake"]

food = [drinks, dinner, desert]
print(food[1])          # Indexing the second list from the list food -> dinner
print(food[0][1])       # Indexing the second value from the first list -> drinks -> coffee

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tuple = unchangable, ordered, used to group together related data

student = ("Captain", 21, "female")

print(student.count("Captain"))     # Counting how many times the value I'm seraching for is in the tuple
print(student.index("female"))      # Finding the value by the index of the value

for x in student:
    print(x)

if "Captain" in student:
    print("Captain is here!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Set = collection which is unordered, unindexed. No duplicate values // Is faster then list

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")                  # Adding tha value to the set
utensils.remove("fork")                 # Removing the value
utensils.clear()                        # Deleting all the values from the set

utensils.update(dishes)                 # Setting another set
dinner_table = utensils.union(dishes)   # Adding one set to another

print(utensils.difference(dishes))        # What does utentials have that dishes has not
print(utensils.intersection(dishes))      # WHat does utentials and dishes have in common?

for x in dinner_table:
    print(x)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary = a changable, unordered collection of unique key:value pairs. Fast.

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Bejing",
            "Ukraine": "Kyjev"}

capitals.update({"Czech Republic":"Prague"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")               # Will remove the value
capitals.clear()                    # Will remove everything

print(capitals["Ukraine"])          # Finding the value by it's key
print(capitals.get("Germany"))      # Check if the key is in the dictionary
print(capitals.keys())              # Printing all the keys
print(capitals.values())            # Printing all the values
print(capitals)                     # Printing all the dict
print(capitals.items())             # Printing all the dict

for key, value in capitals.items(): # Not capitals, but capitals.items()
    print(key, value)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Index operator [] = gives access to a sequence's element (str, list, tuples)

name = "captain Leo"

if(name[0].islower()):
    name = name.capitalize()
    
print(name)

first_name = name[:7].upper()
last_name = name[8:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function = a block of code which is executed only whrn it is called.

def hello(name):                                # The structure of the function
    print(f"Hello {name}!\nHave a nice day!")
    

name = input("What is your name?: ")            # Input into the var for next usage
hello(name)                                     # The call of the function

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Return statement = functions send python values/objects back to the caller. These values/objects are known as the function's return value.

def multiply(num1, num2):
    result = num1 * num2
    return result
    
print(multiply(8, 6))

----

def multiply(num1, num2):
    return num1 * num2          # The value will return to a x

x = multiply(8, 6)

print(x)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Keyword arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments. Python knows the names of the arguments that our function recieves.

def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}!")

hello(first="Captain", middle="Kate", last="Leo")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nested functions calls = function calls inside other function calls. Innermost function calls are resolved first.Returned value is used a argument for the next outer function.

print(round(abs(float(input("Enter a whole positive number: ")))))

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Scope = the region that a variable is recognized. A variable is only available from inside the region it is created. A global and locally scoped versions of a var can be created

name = "Captain"        # Global scope (available inside & outside func)

def display_name():
    name = "Leo"        # Local scope (available only inside this func)
    print(name)
    
display_name()
print(name)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# *args = parameter that will pack all arguments into a tuple. Useful so that a func can accept a varying amount of args

def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1,2))

def plus(*args):        # Important to have * , the name could be whatever
    sum = 0             # args is a tuple (unmutable)
    for i in args:
        sum += i
    return sum

print(plus(1, 2, 3, 4, 5, 6, 7, 8))

def pluss(*args):       # Important to have * , the name could be whatever
    sum = 0
    args = list(args)   # args is a list (mutable)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(pluss(1, 2, 3, 4, 5, 6, 7, 8))

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# **kwargs = parameter that will pack all args into dict. Useful so that a func can accept a varying amount of keyword args

def hello(first, last):
    print(f"Hello {first} {last}")

hello(first="Captain", last="Leo")

def helllo(**kwargs):                           # Important to have ** in name, the name is not important at all
    # print(f"Hello {kwargs['first']} {kwargs['last']}")
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
    
helllo(title="Mrs", first="Captain", middle="Kate", last="Leo")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# str.format() = optional method that gives users. More control when displaying output.

animal = "cow"
item = "moon"

print(f"The {animal} jumped over the {item}")
print("The {} jumped over the {}".format("cow", "moon"))
print("The {1} jumped over the {0}".format(animal, item))
print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Captain"
print("Hello! My name is {}".format(name))
print("Hello! My name is {:10}. Nice to meet you.".format(name))
print("Hello! My name is {:<10}. Nice to meet you.".format(name))
print("Hello! My name is {:>10}. Nice to meet you.".format(name))
print("Hello! My name is {:^10}. Nice to meet you.".format(name))
print("Hello! My name is {:10}. Nice to meet you.".format(name))

number = 314159
print("The number is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:E}".format(number))

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Random library

x = random.randint(1,6)         # The last digit is include!
y = random.random()

myList = ["Rock", "Paper", "Scissors"]
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(f"{e}\nYou can't devide by 0.")
except ValueError as e:
    print(f"{e}\nEnter only numbers, please!")
except Exception as e:
    print(f"{e}\nSomething went wrong.")
else:
    print(result)
finally:
    print("This will always execute")
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# OS library

path = "C:\\Users\\user\\Desktop\\test.txt"     # Windows ver

if os.path.exists(path):
    print("This path exists!")
    if os.path.isfile(path):
        print("This is file!")
    elif os.path.isdir(path):
        print("This is a directory!")
else:
    print("This path does not exist!")
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Working with files through Python

with open('Why.txt') as file:       # Automatically closes the file after reading them
    print(file.read())
    
print(file.closed)                  # To check if the file is closed

try:
    with open('Why.tx') as file:       
        print(file.read())
except FileNotFoundError:
    print("File does not exist!")
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Writing into the file in Python

text = "This text has been overwritten"         # This text will be overwritten again

with open('test.txt', 'w') as file:             # w -> write / r -> read
    file.write(text)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Copying files in Python / shutil module

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)

shutil.copyfile('test.txt', 'copy.txt')       # (src.dst, cp.dst)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Moving files in Python / os

source = "test.txt"
destination = " "

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source,destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} was not found")
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Removing files in Python

path = "test.txt"

try:
    os.rmdir(path)          # Remove the directory
    os.remove(path)         # Remove the file
    shutil.rmtree(path)     # Remove a directory cotaining file
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to delete that!")
except OSError:
    print("You cannot delete taht using this func!")
else:
    print(f"{path} was deleted!")
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Module = a file containing python code. May contain funcs, classess, etc. 

import hello
hello.hello()
hello.bye()

import hello as h
h.hello()
h.bye()

from hello import *
hello()
bye()

help("modules")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rock, Paper, Scissors game

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock/paper/scissors?: ").lower()

if player == computer:
    print(f"Computer - {computer}")
    print(f"Player - {player}")
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Computer wins!")
    else:
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Player wins!")
elif player == "scissors":
    if computer == "rock":
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Computer wins!")
    else:
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Player wins!")
elif player == "paper":
    if computer == "scissors":
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Computer wins!")
    else:
        print(f"Computer - {computer}")
        print(f"Player - {player}")
        print("Player wins!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Better version
        
symbols = ["R", "P", "S"]
player = input(f"Choose one of the symbols - {symbols}: ").upper()
ai = random.choice(symbols)

if player == ai:
    print(f"Plyer: {player} / AI: {ai}")
    print("Tie!")
elif (player, ai) in [("R", "S"), ("S", "P"), ("P", "R")]:
    print(f"Plyer: {player} / AI: {ai}")
    print("Player won!")
else:
    print(f"Plyer: {player} / AI: {ai}")
    print("AI won!")
    
# For a infinity tries of game - while loop 
# -> while True:
#  play_again = input("Do you want to play again? yes/no: ").lower()
#  if play_again != "yes"
#    break
#  print("")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Basic Quizz Game

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:       # The key part is important!
        print("--------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input(f"Enter A/B/C: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        
    display_score(correct_guesses, guess)
        
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("Results")
    print("--------------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is {score}%.")
    
def play_again():
    response = input("Do you want to play again? Yes/No: ").lower()
    
    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth flat?: " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"], 
           ["A. 1989", "B. 1991", "C. 2016"],
           ["A. Smosh", "B. Lonely Island", "C. Monty Python"],
           ["A. True", "B. False", "C. Sometimes"]]

new_game()

while play_again():
    new_game()
    
print("Byeeeeee!")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# OOP Python

from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

print(car_1.make, car_1.model, car_1.year, car_1.color)
print(car_2.make, car_2.model, car_2.year, car_2.color)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class variables

from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.wheels = 2

print(car_1.make, car_1.color, car_1.wheels)
print(car_2.make, car_2.color, car_2.wheels)
print(Car.wheels)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

class Animal:               # Parent class
    
    alive = True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
class Rabbit(Animal):       # Child class from Animal class
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
hawk.sleep()
fish.eat()
hawk.fly()
fish.swim()
rabbit.run()

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multi-level inheritance when a derived (child) class inherits another derived (child) class

class Organism:
    
    alive = True
    
class Animal(Organism):
    
    def eat(self):
        print("This animal is eating")
        
class Dog(Animal):
    
    def bark(self):
        print("This dog is barking")
        
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    
    def flee(self):
        print("This animal flees")
        
class Predator:
    
    def hunt(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method overwriting

class Animal:
    
    def eat(self):
        print("This animal is eating")
        
class Rabbit(Animal):
    
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method chaining = calling multiple methods sequentially. Each call performs an action on the same object and returns self

class Car:
    
    def turn_on(self):
        print("You start the engine")
        return self   
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()
car.turn_on()
car.drive()

car.turn_on().drive()           # Need to return self in funcs

car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()
            
--------------------------------------------------------------------------------------------------------------------------------------------------------------

# super() = Function used to give access to the methods of a parent class. Returns a temporary object a parent class when used.

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Square(Rectangle):
    
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
        return self.length*self.width
    
class Cube(Rectangle):
    
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def volume(self):
        return self.length*self.width*self.height
        
square = Square(3, 3)
cube = Cube(3, 3, 3)
print(square.area())
print(cube.volume())

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Abstract classes = prevents a user from creating an object of that class + compels a user to override abstract methods in a child class
# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("You drive the car")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
        
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()




"""

class Pes:

    krmivo = ['granule', 'maso', 'gauc']            #verejny datovy clen tridy

    def __init__(self, jmeno, majitele, zvuk_stekani):
        self._jmeno = jmeno                         #chraneny datovy clen instance
        self.majitele = majitele                    #verejny datovy clen instance
        self.__zvuk_stekani = zvuk_stekani          #privatni datovy clen instance
        self._vek = 0
        self._prikaz = None

    def stekej(self):                               #veřejná metoda instance
        return self.__zvuk_stekani                    

    def __zmen_zvuk(self, novy_zvuk):               #privatní metoda instance
        self.__zvuk_stekani = novy_zvuk               

    #jmeno bude read-write - jmeno muzeme menit a pes nam ho obcas i prozradi nebo stekne :)
    @property                                       #definice verejne vlastnosti (accessor)
    def jmeno(self):                                
        return self._jmeno if random.random() > 0.5 else "Haf???"

    @jmeno.setter                                   #definice verejne vlastnosti (mutator)
    def jmeno(self, value):
        if value != "Jonatan":                      #pes se vsak nechce jmenovat Jonatan :))
            self._jmeno = value

    #vek bude read-only - vek nemuzeme jako verejnost nastavit, pes musi starnout
    @property
    def vek(self):
        self._vek += 1
        if self._vek >= 5:
            self.__zmen_zvuk("GRAAAAWWWWW HAAAAAF VRRRRR")
        return self._vek

    #prikaz bude write-only (pes nam nemuze rict, co jsme mu prikazali)
    @property
    def prikaz(self):
        raise AttributeError('unreadable attribute')

    @prikaz.setter
    def prikaz(self, value):
        self._prikaz = value

    @classmethod                            
    def pridej_krmivo(cls, krmivo):                 #verejna metoda tridy
        cls.krmivo.append(krmivo)           

    @staticmethod
    def jak_dela_pes():                             #verejna staticka metoda
        return "haf haf"                    

azor = Pes(jmeno="Azor", majitele=None, zvuk_stekani="haf haf mnau?")
print(azor.stekej())

print(azor.__zmen_zvuk("haf"))  #volani privatni metody instance

azor.jmeno = "Jonatan"  #nastaveni nove hodnoty mutatorem
print(azor.jmeno)       #volani hodnoty accessorem
azor.jmeno = "Rex"
print(azor.jmeno)

print(azor._vek)                #volani chranene promenne instance (bohuzel Python umozni)

azor.vek = 20                   #nastaveni read-only vlastnosti

print(azor.vek)                 #volani read-only vlastnosti, ktera internet nastavuje privatni promennou
print(azor.stekej())            #volani verejne metody instance

azor.prikaz = "k noze"          #nastaveni write-only vlastnosti

print(azor.prikaz)              #cteni write-only vlastnosti

