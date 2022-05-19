# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/18/2022
# Description: Returns asked for employee information using the key(employee ID number).
#

class Employee:
    """calls information from each employee lists"""

    def __init__(self, name, ID_number, salary, email):

        self._name = name

        self._ID_number = ID_number

        self._salary = salary

        self._email_address = email

    def get_name(self):
        return self._name

    def get_ID_number(self):
        return self._ID_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address

def make_employee_dict(list_names, list_ID, list_salary, list_email):
    """"calls information from Employee and returns dictionary for the key"""
    employee_dict = {}

    list_len = len(list_ID)

    for lp in range(list_len):

       name = list_names[lp]

       id_num = list_ID[lp]

       salary = list_salary[lp]

       email = list_email[lp]

       employee_dict[id_num] = Employee(name, id_num, salary, email)

    return employee_dict

#emp_names = ["Jean", "Kat", "Pomona"]
#emp_ids = ["100", "101", "102"]
#emp_sals = ["30", "35", "28"]
#emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
#result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
#print(result["100"].get_salary())