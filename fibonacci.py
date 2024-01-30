def fibonacci_sequence(max_value):
    # Validate input
    if max_value < 0:
        return "Fibonacci sequence is not defined for negative integers."
    elif max_value == 0:
        return [0]

    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence using a while loop
    while sequence[-1] + sequence[-2] <= max_value:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))   # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))   # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Error message
