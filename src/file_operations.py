import json

def load_shifts_from_file(file_path):
    """ Load shifts from JSON file 
    Parameters: file_path: Path to the JSON file
    Return: List of shifts added or an empty list if an error occurs
    """
    try:
        with open(file_path, 'r') as file:
            shifts = json.load(file)
            print("\nLoaded shifts successfully!")
            return shifts
    except FileNotFoundError:
        print(f"File not found: {file_path}. Starting with an empty shift list")
        return []

def save_shifts_to_file(file_path, shifts):
    """Save shifts to JSON file"""
    try:
        with open(file_path, 'w') as file:
            json.dump(shifts, file, indent=4)
            (print("\nShifts saved successfully!"))
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")