# Write a function that checks if a number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example
print(check_even_odd(3))  # Output: Odd
