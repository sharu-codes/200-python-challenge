"""
Implement a program to calculate the free number of cups the user gets for 
a specified number of cups bought by the user. In this particular case, the user 
gets 1 cup free for every 6 cups bought. (Example: If the user buys 12 cups, 
he gets 2 cups free as per the Buy 6 Get 1 Free offer, and hence the output 
will be 12+2 = 14 cups)

"""

# Step 1: Take the number of cups bought as input from the user
N = int(input("enter the number of cups bought: "))

# Step 2: Calculate the number of free cups using integer division
free_cups = N//6
total_cups = N + free_cups
print("total number of cups the user gets:", total_cups)
