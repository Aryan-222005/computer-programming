# Write a program to extend a list with another list.
def extend_list(lst1, lst2):
    lst1.extend(lst2)
    return lst1

# Example
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(extend_list(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]
