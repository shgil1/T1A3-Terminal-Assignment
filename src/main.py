from app_operations import convert_time_format, calculate_total_hours, calculate_hours_worked, validate_input, validate_date_format, validate_time_format, display_shifts, add_shift, calculate_hours_for_date, find_start_of_week, validate_name_format
from file_operations import load_shifts_from_file, save_shifts_to_file

# This file path works when you run the program from the executable file
FILE_PATH = '../data/shifts.json'
shifts = load_shifts_from_file(FILE_PATH)

def main():

    # Ask for the employee's name once at beginning of the session to ensure the subsequent data added or queried are specific to this employee
    first_name = validate_input("Enter your first name: ", validate_name_format)
    last_name = validate_input("Enter your last name: ", validate_name_format)

    options = """
    1. Add a shift
    2. Display my shifts
    3. Calculate my total weekly hours
    4. Calculate my total hours for a specific date
    5. Exit
    """

    print(f"Hello {first_name}! Welcome to your shift tracker, what would you like to do today?")

    while True:
        print(options)
        choice = input("Please enter your choice (1-5): ").strip()

        if choice == '1':
            shift = add_shift(first_name, last_name)
            shifts.append(shift)
            save_shifts_to_file(FILE_PATH, shifts)
            print("Shift added and saved successfully!")
        
        elif choice == '2':
            # Filter shifts by the current employee and display
            employee_shifts = [shift for shift in shifts if shift['First_Name'].lower() == first_name.lower() and shift['Last_Name'].lower() == last_name.lower()]
            display_shifts(employee_shifts)
        
        elif choice == '3':
            specific_date = validate_input("Enter the date (dd/mm/yyyy) for which to calculate your weekly hours: ", validate_date_format)
            total_hours = calculate_total_hours(shifts, first_name, last_name, specific_date)
            print(f"\nTotal hours worked by you during the week containing {specific_date}: {total_hours:.2f} hours")
        
        elif choice == '4':
            specific_date = validate_input("Enter a specific date (dd/mm/yyyy) to calculate hours for that day: ", validate_date_format)
            total_hours = calculate_total_hours(shifts, first_name, last_name, specific_date)
            print(f"\nTotal hours worked by you on {specific_date}: {total_hours:.2f} hours")
        
        elif choice == '5':
            print("Ok! Enjoy your day, see you next time!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()