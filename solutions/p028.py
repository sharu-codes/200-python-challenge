"""
Write a python program to check given number is perfect number or not. 

"""

# Step 1: Function to find the sum of all proper divisors of a number
def summation (n):
    sum = 0
    for i in range (1, n):   # Check all numbers from 1 to n-1
        if n % i == 0:       # If i is a divisor of n
            sum += i         # Add it to the sum
    return sum               # Return the sum of proper divisors

# Step 2: Get the number from the user
num = int(input("enter a number: "))

# Step 3: Check whether the number is a perfect number
if num == summation(num):    # A perfect number equals the sum of its proper divisors
    print(num, "is a perfect number")
else:
    print(num, "isn't a perfect number")