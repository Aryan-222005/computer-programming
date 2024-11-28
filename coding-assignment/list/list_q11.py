# Write a program to find the sum of all even numbers in a list.
def sum_of_even(lst):
    return sum(x for x in lst if x % 2 == 0)

# Example
my_list = [1, 2, 3, 4, 5, 6]
print(sum_of_even(my_list))  # Output: 12
