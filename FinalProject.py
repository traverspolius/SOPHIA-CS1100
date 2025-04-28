
# ------------------------------------------------------------
# Sophia Learning - Introduction to Python Programming
# Touchstone 4: Python Journal Project
# Title: Day Counter
# Description: Use this counter to find the number of 
#              days between today's date and a future date.
# By: Travers Polius 
# Date: 04-27-2025
#-------------------------------------------------------------

from datetime import datetime  # Import the datetime module for date operations

while True:  # Infinite loop to allow multiple inputs until the user chooses to exit
    target_date_str = input("Enter a future date (MM-DD-YYYY) or type 'exit' to quit: ")

    if target_date_str.lower() == "exit":  # Check if the user wants to exit
        print("Exiting program. Goodbye!")  # Inform the user that the program is closing
        break  # Terminate the loop

    try:
        # Convert the user input string into a datetime object for comparison
        target_date = datetime.strptime(target_date_str, "%m-%d-%Y")
        # Get today's date
        today_date = datetime.today()
        # Calculate the difference between the entered date and today's date
        days_remaining = (target_date - today_date).days

        if days_remaining >= 0:  # Check if the entered date is in the future
            print(f"There are {days_remaining} days until {target_date_str}.")  # Output days remaining
        else:  # If the date has already passed
            print("The date you entered has already passed.")  # Inform the user

    except ValueError:  # Handle cases where the input format is incorrect
        print("Invalid date format. Please use MM-DD-YYYY.")  # Prompt the user to enter a valid format