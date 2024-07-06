import datetime

def convert_time_format(time_str):
    """Convert time from HHMM format to datetime.time object.

    Parameters:
    'time_str': HHMM format without any colons

    Returns: 
    datetime.time: A datetime object representing the time that is provided
    """
    return datetime.datetime.strptime(time_str, "%H%M").time()

def calculate_total_hours(shifts, first_name, last_name, date_str, mode='daily'):
    """ Calculate total hours worked for a particular employee for either the entire week or a single day based on a specific date inputted.

    Parameters:
    'shifts' (list): List of dictionaries, containing details of a shift
    'first_name'(str): First name of employee
    'last_name' (str): Last name of employee
    'date_str'(str): Start date for calculating hours, formatted as DD/MM/YYYY 
    'mode' (str): Mode of calculation daily or weekly, defaults to daily 
    
    Returns:
    'total_hours' (float): Total hours worked within the specified period
    """
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    if mode == 'weekly':
        # Adjust date to the start of the week (Monday)
        start_date = date - datetime.timedelta(days=date.weekday())
        end_date = start_date + datetime.timedelta(days=6)
    else:
        # For daily mode, start and end dates are the same
        start_date = end_date = date
    
    # Calculate total hours
    total_hours = sum(
        shift['Hours_Worked'] for shift in shifts
        if start_date <= datetime.datetime.strptime(shift['Date'], "%d/%m/%Y") <= end_date and
           shift['First_Name'].lower() == first_name.lower() and
           shift['Last_Name'].lower() == last_name.lower()
    )
    return total_hours

def calculate_hours_worked(date_str, start_time_str, end_time_str):
    """Calculate the hours worked for a single shift.

    Parameters:
    'date_str' (str): The date of the shift in the format of DD/MM/YYYY
    'start_time' (str): The start time of the shift in the format of HHMM
    'end_time' (str): SThe end time of the shift in the format of HHMM

    Return: 
    'total_hours' (float): The total hours worked during the shift
    """
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    start_time = datetime.datetime.strptime(start_time_str, "%H%M").time()
    end_time = datetime.datetime.strptime(end_time_str, "%H%M").time()

    start_datetime = datetime.datetime.combine(date, start_time)
    end_datetime = datetime.datetime.combine(date, end_time)

    if end_datetime < start_datetime:
        end_datetime += datetime.timedelta(days=1)  # Adjust for overnight shifts

    duration = end_datetime - start_datetime
    return duration.total_seconds() / 3600.0

def validate_input(prompt, validation_func):
    """Prompt user input and validate it using the provided validation function.
   
    Parameters:
    'prompt' (str): Prompt to display to the user to input data
    'validation_func' (function): A callback function that takes a single string argument and returns a boolean

    Return:
    'user_input' (str): The validated input
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_date_format(date_str):
    """Validate if a string is in correct date format of DD/MM/YYYY
    
    Parameters:
    'date_str' (str): Date string to validate format
    
    Returns:
    Boolean: True if the date string is valid, otherwise False
    """
    try:
        datetime.datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validate_time_format(time_str):
    """Validate time string is in correct time format of HHMM
    
    Parameters: 
    'time_str' (str): Time string to validate format
    
    Returns:
    Boolean: True if the time string is valid, otherwise False
    """
    try:
        datetime.datetime.strptime(time_str, "%H%M")
        return True
    except ValueError:
        return False

def validate_name_format(name_str):
    """ Validate that the name contains only alphabetical characters
     
    Parameters:
    'name_str' (str): Name string to validate format
     
    Returns:
    Boolean: True if the name is valid, otherwise False
    """
    if name_str.isalpha():
        return True
    else:
        print("Names can only contain alphabetic characters. Please do not include space or numbers.")
        return False

def display_shifts(shifts):
    """Display the current shifts in a readable format for the user.

    Parameters:
    'First_Name', 'Last_Name, 'Date', 'Rostered_Start', 'Rostered_End', 'Hours_Worked'
    """
    if not shifts:
        print("No shifts to display.")
        return

    for shift in shifts:
        print(f"{shift['First_Name']} {shift['Last_Name']} - Date: {shift['Date']}, "
              f"Start: {shift['Rostered_Start']}, End: {shift['Rostered_End']}, "
              f"Hours Worked: {shift['Hours_Worked']}")


def add_shift(first_name, last_name):
    """Add a new shift based on user input.
    Function:
    - Creates a new shift record by collecting data (name, date, start time and end time) 
    - Calculates total hours worked
    
    Parameters: 
    'first_name': A string that shows the first name of the employee that is adding the shift
    'last_name': A string that shows the last name of the employee that is adding the shift

    Return:
    - A dictionary containing details about the shift including: First name, Last name, Date, Rostered start, Rostered end and Hours worked for that specific employee based on the data that the user inputs
    - Prints "Shift added successfully!" once the user correctly inputs all the information and the information is saved to the JSON file
    """
    date = validate_input("Date (dd/mm/yyyy): ", validate_date_format)
    start_time = validate_input("Shift Start Time (HHMM, 24-hour format): ", validate_time_format)
    end_time = validate_input("Shift End Time (HHMM, 24-hour format): ", validate_time_format)
    hours_worked = calculate_hours_worked(date, start_time, end_time)
    shift = {
        "First_Name": first_name,
        "Last_Name": last_name,
        "Date": date,
        "Rostered_Start": start_time,
        "Rostered_End": end_time,
        "Hours_Worked": hours_worked
    }
    print("\nShift added successfully!")
    return shift

def calculate_hours_for_date(shifts, date_str):
    """Calculate total hours worked on a given date.
    Function: 
    - Calculates the sum of hours worked by an employee on a given date by scanning list of shifts and totalling hours for shifts that occured on that date

    Parameters:
    'date_str': A str representing the target date for the total hours worked to be calculated formatted as (dd/mm/yyyy)

    Return:
    'total_hours': Float value total number of hours calculated for that specific date
    """
    specific_date = datetime.datetime.strptime(date_str, "%d/%m/%Y")

    total_hours = sum(
        shift['Hours_Worked'] for shift in shifts
        if datetime.datetime.strptime(shift['Date'], "%d/%m/%Y") == specific_date
    )
    return total_hours

def find_start_of_week(date_str):
    """Determine Monday as the start of the week for a given date.
    Function:
    - Allows other functions to calculate hours worked starting from a Monday
    - Substracts number of days that have passed since the last Monday from given date 'date.weekday()' where Monday is '0' and Sunday is '6'
    - 'timedelta' substracts number of days from the date to align to the beginning of the week

    Parameters:
    'date_str': A string representing date, referencing point to be calculated starting from Monday 

    Return:
    'start_of_week': A datetime object calculated by adjusting provided date backward to most recent Monday
    """
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    start_of_week = date - datetime.timedelta(days=date.weekday())  # Adjust to Monday
    return start_of_week
