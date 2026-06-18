"""
Write a python program to check given number is palindrome number or not.

"""

# Step 1: Function to reverse a number
def reverse (n):
    rev = 0                          # Initialize reversed number
    while n > 0:
        r = n % 10                   # Extract the last digit
        rev = (rev * 10) + r         # Append the digit to the reversed number
        n //= 10
    return rev                       # Return the reversed number

# Step 2: Get the number from the user
num = int(input("enter a number: "))

# Step 3: Check whether the number is an palindrome number
if (num == reverse(num)):
    print(num, "is an palindrome number")
else:
    print(num, "isn't an palindrome number")