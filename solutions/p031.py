# Write a python program to check given string is palindrome number or not. 

# Step 1: Define a function to check whether the string is a palindrome
def is_palindrome (str):

    # Reverse the string using slicing
    rev = str[::-1]
    
    # Return True if the original string and reversed string are the same,
    # otherwise return False
    return (rev == str)

# Step 2: Get the string from the user
str = input("enter the string: ")

# Step 3: Check whether the string is a palindrome
if is_palindrome(str):
    print (str, "is a palindrome string!")
else:
    print(str, "isn't a palindrome string!")