# Write a function to sort a dictionary by its values.
def sort_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example
d = {'a': 3, 'b': 1, 'c': 2}
print(sort_by_values(d))  # Output: {'b': 1, 'c': 2, 'a': 3}
