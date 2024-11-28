# Write a function that merges two lists into a dictionary, where the first list is the keys and the second list is the values.
def merge_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example
print(merge_lists_to_dict(['a', 'b', 'c'], [1, 2, 3]))  # Output: {'a': 1, 'b': 2, 'c': 3}
