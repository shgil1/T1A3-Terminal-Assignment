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