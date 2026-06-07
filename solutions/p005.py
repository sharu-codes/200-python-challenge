"""
Implement a program to calculate sum of digits present in the given number. 

"""

# Step 1: Get the input number from the user
num = int(input("enter a number: "))

# Step 2: Initialize a variable to store the sum of digits
sum = 0

# Step 3: Use a while loop to iterate through each digit of the number and add it to the sum variable
while num > 0:
    digit = num % 10  # Get the last digit
    sum += digit       # Add the digit to the sum
    num //= 10         # Remove the last digit

# Step 4: Print the sum of digits
print("sum of digits:", sum)
