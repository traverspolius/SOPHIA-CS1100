
# ------------------------------------------------------------
# Sophia Learning - Introduction to Python Programming
# Touchstone 4: Python Journal Project
# Title: Day Counter
# Description: Use this counter to find the number of 
#              days between today's date and a future date.
# By: Travers Polius 
# Date: 04-27-2025
#-------------------------------------------------------------

from datetime import datetime

while True:  # Loop to allow multiple inputs until exit condition is met
    target_date_str = input("Enter a future date (MM-DD-YYYY) or type 'exit' to quit: ")

    if target_date_str.lower() == "exit":  # Check for exit condition
        print("Exiting program. Goodbye!")
        break  # Exit the loop

    try:
        target_date = datetime.strptime(target_date_str, "%m-%d-%Y")
        today_date = datetime.today()
        days_remaining = (target_date - today_date).days

        if days_remaining >= 0:
            print(f"There are {days_remaining} days until {target_date_str}.")
        else:
            print("The date you entered has already passed.")

    except ValueError:
        print("Invalid date format. Please use MM-DD-YYYY.")