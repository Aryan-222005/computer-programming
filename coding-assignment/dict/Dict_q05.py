# Write a function to find keys that are common in two dictionaries.
def common_keys(d1, d2):
    return set(d1.keys()) & set(d2.keys())

# Example
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(common_keys(d1, d2))  # Output: {'b'}
