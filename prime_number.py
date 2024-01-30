def is_prime(number):
    # Check for numbers less than 2 (not prime)
    if number < 2:
        return False
    
    # Check for prime numbers
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Test cases
print(is_prime(11))  # Expected output: True
print(is_prime(4))   # Expected output: False
print(is_prime(2))   # Expected output: True
print(is_prime(1))   # Expected output: False
