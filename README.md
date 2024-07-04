# T1A3-Terminal-Assignment
# Shift Management System

## Overview:
- This Python app is designed to allow employees to log and track their shifts. It provides functionalities to add shifts, calculate total hours worked for an entire week or a specific day and display all shifts for a logged-in employee

### Feature 1: User Menu Options:
- Upon starting the application, users are presented with a clear and conscise menu detailing 5 options to choose from:
#### 1. Add a shift
#### 2. Display my shifts
#### 3. Calculate my total weekly hours
#### 4. Calculate my total hours for a specific date
#### 5. Exit

- Users can navigate through these options by entering the number corresponding to their choice, making it easy to use 
- After selecting an option and completing the action, the users are brought back to the main menu which allows them the option to select another function or exit the app
- The menu system uses a loop that continues to display the options until the user selects number 5 to exit the app
- Conditional statements (if, elif, else) inside the loop react to user input to call the appropriate functions

### Feature 2: User can add shift details
- Users are able to input their rostered shift hours and specify the date, start and end times
- The user will input their first and last name, date and start/end times for a shift. The app will then calculate the hours worked based on the start and end times and then save the shifts to the JSON file

### Feature 3: Display all shifts
- Users are able to select from the menu to see all shifts for the current logged-in employee
- The app will filter all the shifts to match those with the name of the logged-in employee and display them

### Feature 4: Calculate total weekly hours worked
- Calculates the total hours worked in one week from Monday to Sunday containing a specified date that is inputted by the user
- Adjusts the provided data to identify the week as starting on a Monday and ending on Sunday then calculates hours worked for shifts falling within that week

### Feature 5: Calculate total hours from a specific date:
- Users can input a date and see how many hours they worked on that specific date

### Feature 6: Error handling for user input and file operations 
- Input validation ensures that users input match expected format

#### 1. 'validate_date_format':
        - Ensures users can only input correct data in the format of dd/mm/yyyy
        - Utilises try block to parse 'date_str' into 'datetime.datetime' object using 'date_str, "%d/%m/%Y"' to check format is correct and returns a boolean
        - Utilises except block to catch any errors to prevent app from crashing 

#### 2. 'validate_time_format':
        - Ensures users can only input correct data of HHMM
        - Utilises try block to parse 'date_str' into 'datetime.datetime' object using 'date_str, "%H%M"' to check format is correct and returns a boolean
        - Utilises except block to catch any errors to prevent app from crashing 

#### 3. 'validate_name_format':
        - Ensures users can only input alphabetic characters withut any spaces or numbers
        - Utilises conditional statements (if, else)
        - if false, the function executes an else block and prints an error message to users stating "Names can only contain alphabetic characters. Please do not include space or numbers."

### Feature 7: Save to JSON file 
- Save all user-entered shift data to an external JSON file so data is not lost when the application is closed 
- Collate all current shift data and convert into JSON format
- 'json.dump' is used to convert the list of dictionaries ('shifts_data') into JSON formatted string and write it directly to a file
- 'indent=4' makes it human-readable and provides consistency across the application 
- 'try-except' block catches and reports errors during file operations 

### Feature 8: Load data from JSON file 
- Retrieve previously saved shift data from JSON file
- Checks and reads the file, if the file exists then the application opens and reads the JSON file
- The reconstructed data is loaded and made available for use 






## Help Documentation:
- Decribe how to use and install the application
- Steps to install the application 
- Any dependencies required by the application to operate 
- Any system/hardware requirements 
- How to use any command line arguments made for the application 



## Implementation plan in chronological order:

### Feature 1: Load data from JSON file
- Create a JSON file and relevant data
- Loading the data is the first step to set up the application with the necessary data and allows for immediate testing as existing shift data is available for processing and display right from the start
- Then start writing the file_operations.py and define load_shifts_from_file with the FILE_PATH parameter
- Utilising the example application demonstrated in the lecture as reference for how to correctly write this

### Feature 2: Save shifts to JSON file
- Implementing save functionality so the data that the user inputs will be immediately updated and saved to the JSON file 
- Creating this early will ensure that any data modified or added during development and testing isn't lost and can be used to test for errors
- Define save_shifts_to_file with the FILE_PATH parameter in file_operations.py 
- Utilising the example application demonstrated in the lecture as reference for how to correctly write this

### Feature 3: User Menu Option
- Create a user menu option and outline the core functionalities of the app

### Feature 4: Add Shift
- Core functionality that allows users to add new shift data 
- This will then add and save data to the JSON file 

### Feature 5: Display all shifts
- Once users add shift details, displaying all relevant shift details based upon the employee's name verifiys data

### Feature 6: Calculate total weekly hours worked
- This feature builds upon feature 3 and 4, allowing users to see a weekly calculation of hours they have worked once inputting a date that can be used for reports and analytics

### Feature 7: Calculate total hours worked
- Implementing this feature builds on the total weekly hours worked option but allows more flexibility in retrieving retrospective data

### Feature 8: Error handling for User input and File operations
- Conduct robust error handling and testing to ensure the app doesn't crash for critical errors and any invalid input information 

## Screenshots:
### Initial app idea layout on paper
![App idea](image.png)

### Trello
![Trello screenshot 1](image-1.png)
![Trello screenshot 2](image-2.png)





















### Virtual Environments
- Help create isolated environments for projects, ensuring each project has its own dependencies (each packages you install for yourself)

## Pytest
- Power and user-friendly testing framework 
- Simple yet powerful package/library 
- Assert (logic/condition true or false value if its true then nothing happens, if its false then it throws an assertion error message)
- Use assert in project testing, make sure our logic is working properly to make sure the output retrieved is the output we expected
- Pytest follows the principle of asserting and that things are true in order for a test to pass, for a test to pass the assert value must be true 

## Error Handling
- Try 
- Value error 

## Initialising 
- Initialising packages to use them in other folders  

## File Handling 
- Read and write data from and to files 
- Open file first, make changes and then close the files 

## Referenced Sources
- https://docs.python.org/3/library/os.html

## Link to source control repository 

## Code style guide or styling conventions that the application will adhere to (rerference chosen style guide appropriately)

## Commenting 
- Indention
- Define function, what is it about, what types of argument it accepts, and what output you expect from that specfic function  

## Important things to note for the README:
- And generally, for the class: just remembering the portfolio submissions -- please, please, please, confirm that you can run your submission in its submission structure before submitting it. We can NOT edit your submissions. If your submission does not work for you, it will not work for us. 

- Part of the assessment is to write instructions on how to run your app - this is what those instructions should be for. 
If we have to cd into a specific directory to run things, make sure that's noted.

- If you feel like you have to completely rearrange your project to meet the submission structure: stop. Just make new folders for the submission ZIP, move your terminal project into the src folder of the submission folders, and make sure the instruction in the submission readme says to cd into the src/YourProjectHere folder.