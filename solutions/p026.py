"""
Given a maximum of four digits to the base 17 (10 - A, 11 - B, 12 - C, 13 - D … 16 - G} as input
output its decimal value. 
input - 1A 
Expected Output - 27 

"""

# Step 1: Create a mapping for base-17 symbols A to G
mapping = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 17
}

# Step 2: Get the base-17 number from the user
num = input("enter a 4 digit number to the base 17: ")

# Step 3: Initialize variables
dec = 0    # Stores the decimal equivalent
i = 0      # Index used to traverse the string

# Step 4: Process each character of the input number
while (i < len(num)):

    # Step 5: Check if the current character is a digit (0–9)
    if ('0' <= num[i] <= '9'):
        digit = int(num[i]) # Convert character to integer

    # Step 6: Otherwise, it must be A–G
    else:
        digit = mapping[num[i]] # Get its corresponding value from the dictionary

    """
    Alternative using ord():
    digit = ord(num[i]) - ord('A') + 10
    Example:
    A → ord('A') - ord('A') + 10 = 10
    B → ord('B') - ord('A') + 10 = 11
    G → ord('G') - ord('A') + 10 = 16
    """

    # Step 7: Convert base-17 to decimal
    dec = dec * 17 + digit

    # Step 8: Move to the next character
    i += 1

# Step 9: Display the decimal value
print("the decimal value is:", dec)