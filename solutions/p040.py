#  Write a python program to find out prime factor of given number. 

import math

# Step 1: Define a function to check whether a number is prime
def is_prime (num):

    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range (2, int(math.sqrt(num)) + 1, 1):

        # If the number is divisible by any value, it is not prime
        if num % i == 0:
            return False
        
    # If no factors are found, the number is prime
    return True

# Step 2: Define a function to find the prime factors
def prime_factor(num):

    # Create an empty list to store the prime factors
    factors = []
    for i in range (2, num + 1):

        # If the number is both a factor and prime, add it to the list
        if num % i == 0 and is_prime(i):
            factors.append(i)

    # Return the list of prime factors
    return factors

# Step 3: Get the number from the user
num=int(input("enter a number: "))

# Step 4: Call the function to find the prime factors
factors=prime_factor(num)
print("the prime factors are: ", end='')

# Step 5: Display the prime factors
for i in factors:
    print(i, end=' ')
