#  Write a python program to find out power of number without pow or **

def power (base, exp):
    res = 1

    for i in range (exp):
        res *= base

    return res

base = int(input("enter a base: "))
exp = int(input("enter an exponent: "))
result = power(base, exp)
print(f"{base} ^ {exp} = {result}")