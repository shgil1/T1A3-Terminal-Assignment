from app_operations import convert_time_format, calculate_total_hours, calculate_hours_worked, validate_input, validate_date_format, validate_time_format, display_shifts, add_shift, calculate_hours_for_date, find_start_of_week, validate_name_format
from file_operations import load_shifts_from_file, save_shifts_to_file

def main():
    file_path = "./shifts.json"
    shifts = load_shifts_from_file(file_path)

    print("Hello! Welcome to your shift tracker, what would you like to do today?")
    options = """
    1. Add a shift
    2. Display all shifts
    3. Calculate your total weekly hours
    4. Calculate your total hours from a specific date
    5. Exit
    """
    while True:
        print(options)
        choice = input("Please enter your choice (1-5): ").strip()

        if choice == '1':
            first_name = validate_input("First Name: ", validate_name_format)
            last_name = validate_input("Last Name: ", validate_name_format)
            shift = add_shift(first_name, last_name)
            shifts.append(shift)
            save_shifts_to_file(file_path, shifts)
            print("Shift added and saved successfully!")
        
        elif choice == '2':
            display_shifts(shifts)
        
        elif choice == '3':
            date_for_calculation = validate_input("Enter a date (dd/mm/yyyy) to calculate weekly hours from: ", validate_date_format)
            total_hours = calculate_total_hours(shifts, specific_date)
            print(f"\nTotal hours worked for the week of {date_for_calculation}: {total_hours:.2f} hours")