# Write a function that returns all prime numbers up to a given number N.
def primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    return primes

# Example
print(primes_up_to_n(10))  # Output: [2, 3, 5, 7]
