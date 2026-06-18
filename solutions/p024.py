"""
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17….   find Nth Term.

"""

import math

# Step 1: Function to find the nth Fibonacci number
def fibonacci (n):
    a, b = 0, 1   # Initialize first two Fibonacci numbers
    for i in range (n):
        a, b = b, a+b   # Update values: a becomes current term, b becomes next term

    return a   # Return the nth Fibonacci number

# Step 2: Function to check whether a number is prime
def is_prime (n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):   # Check divisors from 2 to √n
        if n % i == 0:
            return False
    return True

# Step 3: Function to find the nth prime number
def nth_prime (n):
    count, num = 0, 2    # count = number of primes found, num = current number

    while True:   # Continue until nth prime is found
        if is_prime(num):     # Checks if the current number is prime
            count += 1        # Increment prime counter
            if count == n:    # If nth prime is reached
                return num    # Return nth prime number
            
        num += 1   # Move to the next number

# Step 4: Get the number of terms from the user
n = int(input("enter the range: "))

# Step 5: Generate the sequence
for i in range(1, n + 1):
    if (i % 2 == 1):  # Odd positions → Fibonacci sequence
        result = fibonacci((i + 1) // 2)
    else:             # Even positions → Prime sequence
        result = nth_prime(i // 2)
    print(result, end = ' ')