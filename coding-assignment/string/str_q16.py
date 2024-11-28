# Write a function to check if a string is alphanumeric (contains only letters and numbers).
def is_alphanumeric(s):
    return s.isalnum()

# Example
print(is_alphanumeric("hello123"))  # Output: True
print(is_alphanumeric("hello 123"))  # Output: False
