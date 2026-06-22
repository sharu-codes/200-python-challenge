# Write a python program to print ASCII value of all characters. 

# Step 1: Loop through all ASCII values from 0 to 255
for i in range(256):

    # Step 2: Convert the ASCII value to its corresponding character using chr()
    # and print both the character and its ASCII value
    print(f"{chr(i)} : {i}")