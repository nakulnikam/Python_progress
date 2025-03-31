# Arithmetic Operations with User Input

# Ask for two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Undefined (division by zero)")
