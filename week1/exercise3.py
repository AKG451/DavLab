"""
Create a Python function that creates a sequence between 1 and
100 and prints all the odd numbers. Compute and display the sum
of all the even numbers.
"""

def sequencer(a):
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
        if(i%2==0):
            a+=i
    print(f"The sum of all even numbers between 1 and 100 is {a}")
sum = 0;
sequencer(sum)
