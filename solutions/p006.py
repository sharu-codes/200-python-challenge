"""
Implement a program to calculate sum of even digits present in the given 
number.

"""

# Step 1: Get the input number from the user
num = int(input("enter a number: "))

# Step 2: Initialize a variable to store the sum of even digits
sum_even = 0

# Step 3: Use a while loop to iterate through each digit of the number
# and add it to the sum_even variable if it is even
while num > 0:
    digit = num % 10 # Get the last digit
    if digit % 2 == 0: # Check if the digit is even
        sum_even += digit # Add the even digit to the sum_even variable
    num //= 10 # Remove the last digit

# Step 4: Print the sum of even digits
print("sum of even digits:", sum_even)