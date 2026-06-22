# Write a python program to get factorial of given number. 

# Step 1: Define a function to calculate the factorial of a number
def factorial(n):

    # Initialize factorial as 1
    fact = 1

    # Multiply fact by every number from 1 to n
    for i in range(1, n+1):
        fact *= i

    # Return the calculated factorial
    return fact

# Step 2: Get the number from the user
n = int(input("enter a range: "))
result = factorial(n)

# Step 3: Display the factorial of the given number
print(f"the factorial of {n} is {result}")