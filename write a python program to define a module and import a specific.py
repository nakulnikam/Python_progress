# arithmetic.py
def add(a, b):
 return a + b
def subtract(a, b):
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 if b != 0:

 return a / b
 else:
 return "Division by zero is not allowed"
# main.py
from arithmetic import add, subtract # Importing only the add and
subtract functions
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
result1 = subtract(num1, num2)
print("Sum:", result)
print("Subtract:", result1)