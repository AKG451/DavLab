""" 
Write a Python function to input two numbers and perform the
Calculator operations of (+, -, *, /).
"""

def calculator(a,b):
    add = a+b
    print(f"Addition of {a} and {b} is: {add}")
    sub = a-b
    print(f"Subtraction of {a} and {b} is: {sub}")
    multiply = a*b
    print(f"Multiplication of {a} and {b} is: {multiply}")
    if b!=0:
        division = a/b
        print(f"Division of {a} by {b} is: {division}")
    else:
        print("Since Second number is zero division isn't possible.")

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    calculator(a,b)
except ValueError:
    print("Error: Please enter valid numbers")


