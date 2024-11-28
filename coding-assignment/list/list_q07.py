# Write a program to find the second largest element in a list.
def second_largest(lst):
    lst_sorted = sorted(lst, reverse=True)
    return lst_sorted[1]

# Example
my_list = [10, 20, 4, 45, 99]
print(second_largest(my_list))  # Output: 45
