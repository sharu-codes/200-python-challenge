"""
print the pattern:

    *
  * *
* * *
  * *
    *

"""

# Step 1: Get the number of rows for the pattern from the user
rows = int(input("enter the number of rows: "))

# Step 2: Print the upper half of the pattern (increasing stars)
for i in range (1, rows//2 + 1):  # Loop from 1 up to half of the rows
    for j in range (rows // 2 - i + 1):
        print(" ", end = ' ') # Inner loop to print spaces before the space
    for j in range (i):
        print("*", end = ' ') # Inner loop to print spaces before the stars
    print()

# Step 3: Print the lower half of the pattern (decreasing stars)
for i in range (rows // 2 + 1, 0, -1):  # Loop from middle row down to 1
    for j in range (rows // 2 - i + 1):
        print(" ", end = ' ') # Inner loop to print spaces before the space
    for j in range (i):
        print("*", end = ' ') # Inner loop to print spaces before the stars
    print()
