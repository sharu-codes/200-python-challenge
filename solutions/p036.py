#  Write a python program to find out sum of digit of given number. 

# Step 1: Define a function to find out the sum of digits of a number
def sum_of_digits(n):

    # Initialize the sum variable as 0
    sum = 0

    # Continue until all digits of the number are processed
    while (n>0):

        # Extract the last digit of the number
        rem = n % 10
        # Add the last digit to the sum variable
        sum += rem
        # Remove the last digit from the original number
        n //= 10
    return sum

# Step 2: Get the number from the user
n = int(input("enter the number: "))
result = sum_of_digits(n)

# Step 3: Display the sum of the digits of the number
print(f"the reverse of {n} is {result}")