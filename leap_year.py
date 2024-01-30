def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is a century year
        if year % 100 == 0:
            # Check if the century year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test cases
print(is_leap_year(2020))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2019))  # Expected output: False
