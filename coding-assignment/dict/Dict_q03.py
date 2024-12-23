# Write a function to invert a dictionary (swap keys and values).
def invert_dict(d):
    return {v: k for k, v in d.items()}

# Example
d = {'a': 1, 'b': 2, 'c': 3}
print(invert_dict(d))  # Output: {1: 'a', 2: 'b', 3: 'c'}
