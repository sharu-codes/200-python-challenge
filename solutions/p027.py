"""
Replace all 0's with 1 in a given integer and vice-versa

"""

# Step 1: Get the number as a string from the user
num = input("enter a number: ")

# Step 2: Create an empty string to store the modified number
result = ""

# Step 3: Traverse each digit of the input number
i = 0
while i < len(num):

    # Step 4: If the current digit is 0, replace it with 1
    if num[i] == '0':
        result += '1'

    # Step 5: Otherwise, replace it with 0
    # (Assumes the input contains only 0s and 1s)
    else:
        result += '0'
    i += 1

# Step 6: Display the modified number
print(result)