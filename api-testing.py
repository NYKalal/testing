# Input two integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Addition
addition = a + b

# Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b

# Division
if b != 0:
    division = a / b
else:
    division = "Cannot divide by zero"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# This is version 3