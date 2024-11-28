# Write a function to add a new key-value pair to a dictionary.
def add_pair(my_dict, key, value):
    my_dict[key] = value
    return my_dict

# Example
my_dict = {'a': 1, 'b': 2}
print(add_pair(my_dict, 'c', 3))  # Output: {'a': 1, 'b': 2, 'c': 3}
