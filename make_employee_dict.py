class Employee:

    def __init__(self, name, ID_number, salary, email):

       #Set the values of

       #the data members of the class.

        self.__name = name

        self.__ID_number = ID_number

        self.__salary = salary

        self.__email_address = email

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email_address

#Define the function

#make_employee_dict().

def make_employee_dict(list_names, list_ID, list_salary, list_email):

   #Define the dictionary

   #to store the results.

   employee_dict = {}

   list_len = len(list_ID)

   for lp in range(list_len):

       name = list_names[lp]

       id_num = list_ID[lp]

       salary = list_salary[lp]

       email = list_email[lp]

       employee_dict[id_num] = Employee(name, id_num, salary, email)


   return employee_dict

emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_name())