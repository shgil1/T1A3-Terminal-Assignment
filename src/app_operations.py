import datetime

def convert_time_format(time_str):
    """Convert time from HHMM format to datetime.time object.
    Function:
    - Converts string representing 24 hour time without any colons into datetime.time object

    Parameters:
    'time_str': HHMM format intended to eliminate errors and confusion when handling time-related operations and the expected outcome is a readable time
    """
    return datetime.datetime.strptime(time_str, "%H%M").time()



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


def add_shift(first_name, last_name):
    """Add a new shift based on user input."""

