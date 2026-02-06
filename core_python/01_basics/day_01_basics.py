'''
Day 1: Basics of Python
Focus:
- Variables and Data Types
- Input/Output
- Type casting


Kay Learnings:
1. Input is always a string, so we need to cast it to the appropriate type.'''


# Exercise 1: Variables and Data Types
age = 25
height = 5.9
name = "Python"
is_learning = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_learning))


# Exercise 2: Input/Output
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

current_year = 2026
age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")


# Exercise 3: Type Casting
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
print(int(a) + int(b))

# Exercise 4: Simple Arithmetic
x = 10
y = 3

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# Exercise 5: Mini Task - temperature converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")