#  Write a function that checks if a number is positive, negative, or zero.
def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example
print(check_sign(-5))  # Output: Negative
