"""
print the pattern:

      * 
    * * * 
  * * * * * 
* * * * * * * 

"""

# Step 1: Get the number of rows for the pattern from the user
rows = int(input("enter the number of rows: "))

# Step 2: Use a nested loop to print the pattern
for i in range (1, rows + 1): # Outer loop to iterate through each row
    for j in range (rows - i): # Inner loop to print spaces before the stars
        print (" ", end = ' ')
    for j in range (i): # Inner loop to print the stars in each row
        print ("*", end = ' ')
    for j in range (i - 1): # Inner loop to print the stars in each row (except the first star)
        print ("*", end = ' ')
    print() # Move to the next line after printing all spaces and stars in the current row