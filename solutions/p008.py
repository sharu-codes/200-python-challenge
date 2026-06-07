"""
Implement a program to check prime or not.
 
"""

# Step 1: Get the input number from the user
num = int(input("enter a number: "))

# Step 2: Check if the number is less than or equal to 1
if num <= 1:
    print(num, "is not a prime number.")
else:
    # Step 3: Check if the number is divisible by any number from 2 to the square root of the number
    is_prime = True
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Step 4: Print the result based on the value of is_prime
if is_prime:
    print(num, "is a prime number.")   
else:
    print(num, "is not a prime number.")