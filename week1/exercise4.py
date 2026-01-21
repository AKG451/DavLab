"""
Write a Python function to add two elements and display the
result. The elements can be of type integer, float or string.
"""

def add_elements(element1, element2):
    try:
        result = element1 + element2
        print(f"Input: {element1} ({type(element1).__name__}) + {element2} ({type(element2).__name__})")
        print(f"Result: {result}")
        print("-" * 30) 
        
    except TypeError:
        print(f"Error: Cannot add {type(element1).__name__} with {type(element2).__name__}")

add_elements(10, 20)
add_elements(5.5, 4.5)
add_elements("Hello, ", "World!")
add_elements(10, "Apple")