"""
Given an integer n, perform the following conditional actions, 
If n is odd, print weird, 
If n is even and in the inclusive range of 2 to 5, print not weird, 
If n is even and in the inclusive range 6 to 20, print weird, 
If n is even and greater than 20, print not weird.

"""

# Step 1: Take a number as input from the user

num = int(input("enter a number: "))

# Step 2: Check the conditions and print the result

if num%2!=0:
    print("weird!")
elif num%2 == 0:
    if num in range (2, 6):
        print("not weird!")
    elif num in range (6, 21):
        print("weird!")
    elif num>20:
        print("not weird!")