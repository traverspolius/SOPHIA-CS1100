from datetime import datetime

# Get user input for the target date (YYYY-MM-DD format)
target_date_str = input("Enter a future date (MM-DD-YYYY): ")

try:
    # Convert input string to a datetime object
    target_date = datetime.strptime(target_date_str, "%m-%d-%Y")
    # Get today's date
    today_date = datetime.today()
    # Calculate the difference in days
    days_remaining = (target_date - today_date).days

    if days_remaining >= 0:
        print(f"There are {days_remaining} days until {target_date_str}.")
    else:
        print("The date you entered has already passed.")

except ValueError:
    print("Invalid date format. Please use MM-DD-YYYY.")