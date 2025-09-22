
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:")
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future Date:")
    print(future_date.strftime("%Y-%m-%d"))
def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
if __name__ == "__main__":
    main()