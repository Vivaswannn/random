def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Take user input
num = int(input("Enter a number: "))

# Calculate and print factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the function
number = 5
print(f"Factorial of {number} is {factorial(number)}")

