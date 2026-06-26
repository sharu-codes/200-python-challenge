#  Write a python program to find out power of number without pow or **

# Step 1: Define a function to calculate the power
def power (base, exp):

    # Initialize the result as 1
    res = 1

    for i in range (exp):
        # Multiply the base by itself 'exponent' number of times
        res *= base

    # Return the calculated power
    return res

# Step 2: Get the base and exponent from the user
base = int(input("enter a base: "))
exp = int(input("enter an exponent: "))

# Step 3: Call the function
result = power(base, exp)

# Step 4: Display the result
print(f"{base} ^ {exp} = {result}")