"""
Implement a program to print prime number between range.

"""

# Step 1: Get the input range from the user
start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

# Step 2: Use a for loop to iterate through the numbers in the given range
print ("the prime numbers between", start, "and", end, "are: ", end='')
for num in range (start, end + 1):
    # Step 3: Check if the number is less than or equal to 1
    if num <= 1:
        continue
    else:
        # Step 4: Check if the number is divisible by any number from 2 to the square root of the number
        is_prime = True
        for i in range (2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # Step 5: Print the prime number if is_prime is True
        if is_prime:
            print(num, end=' ')   