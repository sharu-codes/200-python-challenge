# Write a python program to reverse any number

# Step 1: Define a function to reverse a number
def reverse(n):

    # Initialize the reversed number as 0
    rev = 0

    # Continue until all digits of the number are processed
    while (n>0):

        # Extract the last digit of the number
        rem = n % 10
        # Append the extracted digit to the reversed number
        rev = (rev * 10) + rem
        # Remove the last digit from the original number
        n //= 10
    return rev

# Step 2: Get the number from the user
n = int(input("enter the number: "))
result = reverse(n)

# Step 3: Display the reversed number
print(f"the reverse of {n} is {result}")