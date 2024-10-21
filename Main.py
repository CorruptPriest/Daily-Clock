#This is a program to calculate the no. of days to a certain date. 
import datetime
from datetime import datetime
def main():
    # Get today's date
    today = datetime.now()
    
    
    # Default target date: February 1st of the next year
    next_year = today.year + 1 if today.month > 2 else today.year
    default_target_date = datetime(next_year, 2, 1)
    
    print("Today's date:", today.strftime("%d-%m-%Y"))
    
    # Ask user for manual input
    manual_input = input("Set a manual target date? (yes/no): ").strip().lower()
    
    if manual_input == 'yes':
        manual_date_str = input("Enter the target date (DD-MM-YYYY): ")
        try:
            manual_target_date = datetime.strptime(manual_date_str, "%d-%m-%Y")
            days_until = (manual_target_date - today).days
            print(f"Days until {manual_target_date.strftime('%d-%m-%Y')}: {days_until} days")
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
    else:
        days_until_default = (default_target_date - today).days
        print(f"Days until {default_target_date.strftime('%d-%m-%Y')}: {days_until_default} days")

if __name__ == "__main__":
    main()