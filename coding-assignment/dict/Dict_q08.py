# Write a function to remove a key-value pair from a dictionary by key.
def remove_key(my_dict, key):
    if key in my_dict:
        del my_dict[key]
    return my_dict

# Example
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(remove_key(my_dict, 'b'))  # Output: {'a': 1, 'c': 3}
