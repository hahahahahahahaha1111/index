def compound_interest_calculator(P, r, n, t):
    # Validate inputs
    if P <= 0 or r < 0 or n <= 0 or t <= 0:
        return "Invalid input. Please provide valid values for Principal, Annual interest rate, Number of times compounded, and Time."

    # Calculate compound interest
    A = P * (1 + r/n)**(n*t)

    return A

# Test cases
amount_after_5_years = compound_interest_calculator(1000, 0.05, 12, 5)
amount_after_10_years = compound_interest_calculator(500, 0.07, 4, 10)
amount_after_7_years = compound_interest_calculator(1500, 0.03, 6, 7)

print(amount_after_5_years)  # Expected: Amount after 5 years
print(amount_after_10_years)  # Expected: Amount after 10 years
print(amount_after_7_years)  # Expected: Amount after 7 years
