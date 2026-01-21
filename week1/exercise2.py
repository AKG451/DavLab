"""
Write a Python function that takes an integer and returns True if
it’s a prime number and False otherwise.
"""

import math

def isPrime(a):
    if(a>1):
        for i in range(2,int(math.sqrt(a))+1):
            if(a%i==0):
                return False
    else:
        return False
    return True
try:
   a = int(input("Please enter the number you want to check: "))
   result = isPrime(a)
   if result:
        print(f"{a} is True (It is Prime)")
   else:
        print(f"{a} is False (It is not Prime)")
except ValueError:
    print("Error: Enter a valid number")