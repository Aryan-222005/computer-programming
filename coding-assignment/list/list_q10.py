# Write a program to multiply all the elements in a list.
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example
my_list = [1, 2, 3, 4]
print(multiply_elements(my_list))  # Output: 24
