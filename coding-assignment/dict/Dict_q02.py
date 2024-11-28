# Write a function that takes a list of integers and returns a dictionary with the frequency of each number.
def count_frequency(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Example
nums = [1, 2, 2, 3, 3, 3]
print(count_frequency(nums))  # Output: {1: 1, 2: 2, 3: 3}
