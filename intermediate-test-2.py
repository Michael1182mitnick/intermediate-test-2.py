# Implement a recursive function to generate the Fibonacci sequence up to the nth number.

def fibonacci(n):
    # Base case: the first two numbers in the Fibonacci sequence are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the previous two numbers
        return fibonacci(n-1) + fibonacci(n-2)


# Example usage
n = int(input("Enter the value of n: "))
fib_sequence = [fibonacci(i) for i in range(n)]
print(f"The Fibonacci sequence up to the {n}th number is: {fib_sequence}")
