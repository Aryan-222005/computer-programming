# Write a program to merge the tuples (1, 2, 3) and (3, 4, 5) and remove duplicates from the result.
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
merged_tuple = tuple(set(tuple1 + tuple2))
print(merged_tuple)  # Output: (1, 2, 3, 4, 5)
