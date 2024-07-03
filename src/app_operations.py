import datetime

def convert_time_format(time_str):
    """Convert time from HHMM format to datetime.time object.
    Function:
    - Converts string representing 24 hour time without any colons into datetime.time object

    Parameters:
    'time_str': HHMM format intended to eliminate errors and confusion when handling time-related operations and the expected outcome is a readable time
    """
    return datetime.datetime.strptime(time_str, "%H%M").time()

def calculate_total_hours(shifts, period="weekly", specific_date=None, end_date=None):
    """
    Calculate total hours worked for the specified period starting from the given date.
    If the time period is custom, calculate between the specific_date and end_date.
    Function: 
    - Depending on the 'period' parameter, the function determines the start and end dates for the calculation
    - Calculation for 'weekly' and 'fortnightly' options
    - Calculates based on week starting on Monday for the provided 'specific_date' and adjusts 'end_date' accordingly
    - Calulates the hours by iterating through 'shifts' list to check if each shift date falls between 'start_date' and 'end_date', if it does then it is included in the total

    Parameters:
    'shifts': List of dictionaries, each dictionary represents a shift and must include two key-value pairs: date and hours_worked
    'period': A string indicating period type for which total hours should be calculated, defaults to 'weekly'
    'specific_date': A string representing the start date from which the calculation begins (dd/mm/yyyy) if not provided, the current date is used
    'end_date': A string representing the end from which the calculation runs (dd/mm/yyyy) this is only used if the 'period' is set to 'custom'

    Returns:
    'total_hours': Float, Caluclation for the total number of hours worked within the specified period by summing up the 'hours_worked' values for all shifts that fall within the determined date range
    """
    if period == "custom" and specific_date and end_date:
        start_date = datetime.datetime.strptime(specific_date, "%d/%m/%Y")
        end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
    else:
        # Assuming specific_date is provided, find the start of the week
        start_date = datetime.datetime.strptime(specific_date, "%d/%m/%Y") if specific_date else datetime.datetime.now()
        start_date = start_date - datetime.timedelta(days=start_date.weekday())  # Adjust to Monday
        if period == "fortnightly":
            end_date = start_date + datetime.timedelta(days=13)  # Two weeks minus one day
        else:  # default to weekly
            end_date = start_date + datetime.timedelta(days=6)  # One week

    total_hours = sum(
        shift['Hours_Worked'] for shift in shifts 
        if datetime.datetime.strptime(shift['Date'], "%d/%m/%Y") >= start_date and
           datetime.datetime.strptime(shift['Date'], "%d/%m/%Y") <= end_date
    )
    return total_hours

def calculate_hours_worked(date_str, start_time_str, end_time_str):
    """Calculate the hours worked for a single shift.
    Function: 
    - Converts 'date_str', 'start_time_str', 'end_time_str' into 'datetime' objects representing the start and end of the shift
    - Calculates duration of shift by subtracting start time from end time and converting duration from seconds to hours
    - If end time is earlier than the start time for an overnight shift, function adjust to add a day to the end time to calculate correct duration of shift

    Parameters:
    date_str: String for date of shift is expected in the format of dd/mm/yyyy
    start_time_str: String for start of shift is expected in the 24 hour format to avoid confusion for am or pm shifts
    end_time_str: String for end of shift in 24 hour format
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
    Function:
    - Initiates a loop via 'prompt' string to prompt user for input
    - Each input received from the user is passed to the 'validation_func', if true, the input is considered valid and the function breaks out of the loop. If false, the function prints an error message saying "Invalid input. Please try again" and re-prompts the user. This loop ensures the function does not return until it receives valid input

    Parameters:
    'prompt': A string that is displayed to users to input the correct date format (dd/mm/yyyy)
    'validation_func': A callback function that takes a single string argument and returns a boolean

    Return:
    'user_input': This function returns the user input as a string after it has been validated by the 'validation_func' to ensure the output of function is always valid as per the defined criteria 
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def add_shift(first_name, last_name):
    """Add a new shift based on user input."""

