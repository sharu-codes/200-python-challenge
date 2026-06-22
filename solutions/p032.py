# Write a python program to print Fibonacci series of given range.

# Step 1: Define a function to print the Fibonacci series
def fibonacci (n):

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for i in range(n):

        # Print the current Fibonacci number
        print (a, end =' ')

        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b

# Step 2: Get the range (number of terms) from the user
n = int(input("enter a range: "))

# Step 3: Call the function to print the Fibonacci series
fibonacci(n)