"""
Write a python program to check given number is Armstrong number or not.

"""

# Step 1: Function to find the number of digits in a number
def length (n):    # Initialize digit counter
    len = 0
    while n > 0:
        n //= 10
        len += 1
    return len     # Return the total number of digits

# Step 2: Function to calculate the Armstrong sum
def armstrong (n):
    m = n                       # Store the original number
    sum = 0
    while n > 0:
        r = n % 10
        sum += r ** length(m)   # Add digit^(number of digits) to the sum
        n //= 10
    return sum                  # Return the calculated Armstrong sum

# Step 3: Get the number from the user
num = int(input("enter a number: "))

# Step 4: Check whether the number is an Armstrong number
if (num == armstrong(num)):
    print(num, "is an armstrong number")
else:
    print(num, "isn't an armstrong number")