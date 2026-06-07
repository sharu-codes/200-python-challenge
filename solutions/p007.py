"""
Implement a program to calculate sum of odd digits present in the given 
number. 

"""

# Step 1: Get the input number from the user
num = int(input("enter a number: "))

# Step 2: Initialize a variable to store the sum of odd digits
sum_odd = 0

# Step 3: Use a while loop to iterate through each digit of the number
# and add it to the sum_odd variable if it is odd
while num > 0:
    digit = num % 10 # Get the last digit
    if digit % 2 == 1: # Check if the digit is odd
        sum_odd += digit # Add the odd digit to the sum_odd variable
    num //= 10 # Remove the last digit

# Step 4: Print the sum of odd digits
print("sum of odd digits:", sum_odd)