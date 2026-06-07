"""
Implement a program to calculate sum of prime digits present in the given number

"""

# Step 1: Get the input number from the user
num = int(input("enter a number: "))

# Step 2: Function to check if a digit is prime
def is_prime_digit(digit):
    return digit in [2, 3, 5, 7]

# Step 3: Initialize a variable to store the sum of prime digits
sum_of_prime_digits = 0

# Step 4: Iterate through each digit in the input number and check if it is a prime digit
while num > 0:
    digit = num % 10 # Get the last digit
    if is_prime_digit(digit):
        sum_of_prime_digits += digit # Add the prime digit to the sum
    num //= 10 # Remove the last digit

# Step 5: Print the sum of prime digits
print("The sum of prime digits in the given number is:", sum_of_prime_digits)