# Write a function to find the length of a string without using the len() function.
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Example
print(string_length("hello"))  # Output: 5
