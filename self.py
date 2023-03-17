class Employee:
    def employeedetails(self):
        self.name = "Matthew"
        print("Name = ", self.name)
        self.age = 30

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name = ", self.name)
        print("Age = ", self.age)


employee = Employee()
employee.employeedetails()
employee.printEmployeeDetails()