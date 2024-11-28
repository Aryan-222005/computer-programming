# Write a function to get the value associated with a key in a dictionary.
def get_value(my_dict, key):
    return my_dict.get(key, "Key not found")

# Example
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(get_value(my_dict, 'b'))  # Output: 2
print(get_value(my_dict, 'd'))  # Output: Key not found
