# Write a program to count how many times an element appears in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example
my_list = [1, 2, 3, 2, 4, 2]
print(count_occurrences(my_list, 2))  # Output: 3
