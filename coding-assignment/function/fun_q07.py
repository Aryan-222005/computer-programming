# Write a function to count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)

# Example
print(count_vowels("hello"))  # Output: 2
