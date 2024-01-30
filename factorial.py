def calculate_factorial(number):
    # Validate input
    if number < 0:
        return "Factorial is undefined for negative numbers."

    # Initialize factorial result
    factorial_result = 1

    # Calculate factorial using a for loop
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
