# Write a function to print the Fibonacci sequence up to the nth term.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example
fibonacci(5)  # Output: 0 1 1 2 3
