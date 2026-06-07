"""
Implement a program to print nth prime number.
  
"""

# Step 1: A Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Step 2: Get the input n from the user
n = int(input("enter the value of n: "))

# Step 3: Initialize a variable to count the number of prime numbers found and a variable to store the current number being checked
count = 0
num = 1

# Step 4: Use a while loop to find prime numbers until the count of prime numbers found is equal to n
while count < n:
    num += 1              # Increment the number being checked
    if is_prime(num):     # Check if the number is prime
        count += 1        # Increment the count of prime numbers found

# Step 5: Print the nth prime number
print("the", n, "th prime number is:", num)