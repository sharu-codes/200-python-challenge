"""
0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16, 8... find Nth Term. 

"""

# Step 1: Function to generate the integer sequence
def integers (n):
    return n

# Step 2: Function to generate the even-number sequence
def double (n):
    return 2 * n

# Step 3: Get the number of terms from the user
n = int(input("enter the range: "))

# Step 4: Generate the sequence
for i in range(0, n):                         # Loop through positions from 0 to n-1
    if (i % 2 == 0):                          # Even indices (1st, 3rd, 5th... positions)
        result = double ((i + 1) // 2)
    else:                                     # Odd indices (2nd, 4th, 6th... positions)
        result = integers (i // 2)
    print(result, end = ' ')