"""
Write a Python function that takes a string input from the user
and counts the number of vowels and consonants in the string.
"""

def count(a):
    vowels="aeiouAEIOU"
    vcount = 0
    ccount = 0
    for char in a:
        if char.isalpha():
            if char in vowels:
                vcount+=1
            else:
                ccount+=1
    print(f"Original String: {a}")
    print(f"Vowels: {vcount}")
    print(f"Consonants: {ccount}")

word = input("Enter a string: ")
count(word)