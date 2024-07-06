from datetime import datetime

def calculate_days_difference():
    date_format = "%Y-%m-%d %H:%M:%S"
    
    try:
        # Ask user
        date1_str = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
        # Convert the first date string to a datetime object
        date1 = datetime.strptime(date1_str, date_format)
        
        # Ask user
        date2_str = input("Enter the second date and time (YYYY-MM-DD HH:MM:SS): ")
        # Convert the second date string to a datetime object
        date2 = datetime.strptime(date2_str, date_format)
        
        # Calculate the difference between the two dates
        difference = date2 - date1
        # The difference in days
        difference_in_days = difference.days
        
        # Print the difference in days
        print(f"Difference is {difference_in_days} days")
    
    except ValueError as e:
        # Error message
        print("Error... Please enter the date and time in the format YYYY-MM-DD HH:MM:SS")

# Call the function 
calculate_days_difference()
