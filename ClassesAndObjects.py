class Employee: #Defition of Employee Class
    # Define an attribute called name
    name = "Ben"

    def changeName (self):
        # Change the value of the attribute within a method
        Employee.name = "Mark"

employee = Employee() #Create instance of the employee class named employee
print(employee.name)
employee.changeName()
print(employee.name)
