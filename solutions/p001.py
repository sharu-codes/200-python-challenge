"""
Implement a program to check whether the given number is even number 
or odd number. 

"""

# Step 1: Take a number as input from the user

num = int(input("enter a number: "))

# Step 2: Divide it by 2 and check the remainder to determine if it is even or odd

if num % 2 == 0:
    print (num, "is an even number.")
else:
    print (num, "is an odd number.")