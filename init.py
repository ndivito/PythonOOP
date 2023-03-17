class Employee:

    def __init__(self, name):
        self.name = name


    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Mark")
employee.displayEmployeeDetails()
employee2 = Employee("Matthew")
employee2.displayEmployeeDetails()