# Write a function that checks if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# Example
print(is_palindrome("racecar"))  # Output: True
