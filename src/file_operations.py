import json

def load_shifts_from_file(FILE_PATH):
    """ Load shifts from JSON file 
    Parameters: FILE_PATH: Path to the JSON file
    Return: List of shifts added or an empty list if an error occurs
    """
    try:
        with open(FILE_PATH, 'r') as file:
            shifts = json.load(file)
            return shifts
    except FileNotFoundError:
        print(f"File not found: {FILE_PATH}. Starting with an empty shift list")
        return []

def save_shifts_to_file(FILE_PATH, shifts):
    """Save shifts to JSON file"""
    try:
        with open(FILE_PATH, 'w') as file:
            json.dump(shifts, file, indent=4)
    except IOError as e:
        # Handle I/O errors
        print(f"Failed to save shifts: I/O error {e}")
    except TypeError as e:
        # Handle data type errors that json.dump might raise
        print(f"Failed to save shifts: Data type error {e}")
    except Exception as e:
        # General exception catch in cases of unexpected errors
        print(f"An unexpected error occured: {e}")
              