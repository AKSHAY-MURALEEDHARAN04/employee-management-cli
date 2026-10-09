# Employee Data Management CLI

A command-line application developed using Python to manage employee records.

## Features

- Add new employees
- Update employee information
- Delete employees
- Search employees by ID
- Filter employees by department, role, and age
- View all employee records
- Export employee data to JSON
- Export employee data to CSV
- Input validation
- Exception handling
- Application activity logging
- Automated testing using pytest

## Technologies Used

- Python
- JSON
- CSV
- Pytest
- Git

## Project Structure

employee_management_cli/
│
├── data/
│   └── employees.json
│
├── exports/
│   ├── employees.json
│   └── employees.csv
│
├── logs/
│   └── app.log
│
├── tests/
│   └── test_employee_manager.py
│
├── employee_manager.py
├── exporters.py
├── logger.py
├── main.py
├── validators.py
├── requirements.txt
├── .gitignore
└── README.md

## Requirements

- Python 3.13 or higher
- pip
- pytest

## Setup

Create a virtual environment:

python -m venv .venv

Activate the virtual environment on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Install the required packages:

pip install -r requirements.txt

## Running the Application

Run the following command:

python main.py

## Menu Options

1. Add Employee
2. Update Employee
3. Delete Employee
4. Search Employee
5. Filter Employees
6. View All Employees
7. Export to JSON
8. Export to CSV
9. Exit

## Search Employee

Select option 4 and enter the employee ID.

Example:

Enter employee ID to search: EMP001

## Filter Employees

Select option 5.

Employees can be filtered using:

- Department
- Role
- Age

Leave a field blank if you do not want to use that filter.

## Export Data

Select option 7 to export employee data to:

exports/employees.json

Select option 8 to export employee data to:

exports/employees.csv

## Input Validation

The application validates:

- Employee ID
- Employee name
- Age
- Salary
- Email

Invalid input is clearly reported to the user without crashing the application.

## Exception Handling

The application handles expected errors such as:

- Invalid input
- Invalid JSON data
- File reading errors
- File writing errors

## Logging

Application activities and errors are recorded in:

logs/app.log

## Testing

Automated tests are written using pytest.

Run the tests using:

python -m pytest

Current test result:

6 passed

The tests cover:

- Employee ID validation
- Name validation
- Age validation
- Salary validation
- Email validation
- Add employee operation

## Data

The project uses synthetic employee data for demonstration and testing purposes.

No real employee personal information, passwords, API keys, or other secrets are stored in the project.

## Known Limitations

- Employee data is stored in a local JSON file.
- No database is used.
- No authentication system is implemented.
- The application is intended for learning and demonstration purposes.