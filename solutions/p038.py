# Write a python program to add two numbers without using addition operator. 

# Step 1: Define a function to add two numbers
def addition (a, b):

    # Continue until the second number becomes 0
    while b != 0:

        # If the second number is positive
        if b > 0:

            # Increase the first number by 1
            a += 1
            # Decrease the second number by 1
            b -= 1

        # If the second number is negative
        else:

            # Decrease the first number by 1
            a -= 1
            # Increase the second number by 1
            b += 1
    
    # Return the final sum which is stored in the first number variable
    return a

# Step 2: Get two numbers from the user in a single line
num1, num2 = map(int, input("enter two numbers for addition: ").split())

# Step 3: Call the function
sum = addition(num1, num2)

# Step 4: Display the result
print(f"sum of {num1} and {num2} is {sum}")