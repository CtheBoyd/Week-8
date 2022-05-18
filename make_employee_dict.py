class Employee:

    def __init__(self, name, ids, department, title):
        self.__name = name
        self.__ids = ids
        self.__department = department
        self.__title = title

    # set the attributes
    def set_name(self, name):
        self.__name = name

    def set_ids(self, ids):
        self.__ids = ids

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    # return the attributes
    def get_name(self):
        return self.__name

    def get_ids(self):
        return self.__ids

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    # return the objects state as a string

    def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
        return 'Name: ' + self.__name + \
               '\nID number: ' + self.__ids + \
               '\nDepartment: ' + self.__department + \
               '\nTitle: ' + self.__title





emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_name())