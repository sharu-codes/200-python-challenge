# Write a Python program to find the minimum among three numbers using the conditional operator

# Step 1: Get three numbers from the user
num1, num2, num3 = map(int, input("enter three numbers: ").split())

# Step 2: Find the minimum using the conditional (ternary) operator
result = num1 if num1 < num2 and num1 < num3 else (num2 if num2 < num3 else num3)

# Step 3: Display the minimum number
print(f"{result} is the minimum number")