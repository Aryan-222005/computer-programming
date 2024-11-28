#  Write a function to check if a string ends with a specific substring.
def ends_with(s, sub):
    return s.endswith(sub)

# Example
print(ends_with("hello", "lo"))  # Output: True
print(ends_with("hello", "world"))  # Output: False
