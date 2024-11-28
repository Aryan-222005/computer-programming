# Write a program to remove all elements from the tuple (10, 20, 30, 40, 50) that are greater than 30.
my_tuple = (10, 20, 30, 40, 50)
filtered_tuple = tuple(x for x in my_tuple if x <= 30)
print(filtered_tuple)  # Output: (10, 20, 30)
