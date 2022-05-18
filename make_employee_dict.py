class Employee:
    def __init__(self, name, ID, salary, email):
        # assigning name, id, salary and email to private instance variables.
        # private variables in Python are indicated by double underscore before its name
        self.__name = name
        self.__ID = ID
        self.__salary = salary
        self.__email = email

    # getter methods

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email


# make_employee_dict method, which is not part of Employee class. so indentation must be 0
def make_employee_dict(names, ids, salaries, emails):
    # creating a dict
    employee_dict = dict()
    # looping from 0 to len(names)-1
    for i in range(len(names)):
        # creating an Employee using ith elements in all lists as name, id, salary and email
        employee = Employee(names[i], ids[i], salaries[i], emails[i])
        # adding employee to dict with id being the key
        employee_dict[ids[i]] = employee
    return employee_dict


# code for testing
if __name__ == '__main__':
    emp_names = ["Jean", "Kat", "Pomona"]
    emp_ids = ["100", "101", "102"]
    emp_sals = [30, 35, 28]
    emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
    result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
    print(result["100"].get_name())  # should print "Jean"