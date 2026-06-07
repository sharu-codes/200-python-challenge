"""
Implement a program to extract digits from the given number

"""

# Step 1: Take a number as input from the user
num = int(input("enter a number: "))

# Step 2: Reverse the number to extract digits in the original order
rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

# Step 3: Use a while loop to extract digits until the reversed number becomes 0
print("the digits in the number are: ", end='')
while rev_num > 0:
    digit = rev_num % 10
    print(digit, end=' ')
    rev_num = rev_num // 10