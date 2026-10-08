def validate_employee_id(emp_id):
    if not emp_id.strip():
        raise ValueError("Employee ID cannot be empty")
    return emp_id.strip().upper()


def validate_name(name):
    if not name.strip():
        raise ValueError("Employee ID cannot be empty")
    return name.strip()


def validate_age(emp_age):
    emp_age = int(emp_age)
    if emp_age<18 or emp_age>60:
        raise ValueError("Age must between 18 and 60")
    return emp_age


def validate_salary(emp_salary):
    salary=float(emp_salary)
    if salary<0:
        raise ValueError("Salary cant be negative")
    return salary


def validate_email(email):
    if "@" not in email or '.' not in email:
        raise ValueError("Please enter the valid Email address")
    return email.strip()
