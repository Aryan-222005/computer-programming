# Write a program to remove duplicate elements from a list.
def remove_duplicates(lst):
    return list(set(lst))

# Example
my_list = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4]
