"""
print the pattern:

*
* *
* * * 
* * * * 

"""

# Step 1: Get the number of rows for the pattern from the user
rows = int(input("enter the number of rows: "))

# Step 2: Use a nested loop to print the pattern
for i in range(1, rows + 1): # Outer loop to iterate through each row
    for j in range(i): # Inner loop to print the stars in each row
        print("*", end=" ") # Print a star followed by a space, and stay on the same line
    print() # Move to the next line after printing all stars in the current row