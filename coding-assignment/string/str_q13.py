#  Write a function to replace a substring in a string with another substring.
def replace_substring(s, old, new):
    return s.replace(old, new)

# Example
print(replace_substring("hello world", "world", "Python"))  # Output: "hello Python"
