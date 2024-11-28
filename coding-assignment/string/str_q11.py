# Write a function to check if a string starts with a specific substring.
def starts_with(s, sub):
    return s.startswith(sub)

# Example
print(starts_with("hello", "he"))  # Output: True
print(starts_with("hello", "world"))  # Output: False
