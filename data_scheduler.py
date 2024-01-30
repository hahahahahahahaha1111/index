from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Define the date format
    date_format = "%d %B"

    # Extract day and month from the date strings
    today_day, today_month = todays_date.split()
    scheduled_day, scheduled_month = scheduled_date.split()

    # Convert ordinal numbers to integers
    today_day = int(today_day[:-2])
    scheduled_day = int(scheduled_day[:-2])

    # Map month names to their corresponding numeric values
    month_mapping = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }

    # Parse the dates using the defined format
    today = datetime(year=2022, month=month_mapping[today_month], day=today_day)
    scheduled = datetime(year=2022, month=month_mapping[scheduled_month], day=scheduled_day)

    # Compare the dates
    if today == scheduled:
        print("Scheduled date is today")
    elif today > scheduled:
        print("Scheduled date has passed")
    else:
        print("Scheduled date is yet to pass")

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass