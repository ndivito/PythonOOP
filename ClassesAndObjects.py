class Employee:  # Definition of Employee Class
    name = "Nick"  # Created an attribute and assigned it a value

    def diff_name(self):  # Call this Method to change the name
        if self.name == "Kevin":
            print("We need to change the name!")
            self.name = input()
        else:
            print("Perfect, someone who's name is not Kevin!")


employeeOne = Employee()  # Created instance of the Employee Class
print("Your name is", employeeOne.name)  # Calling out the name attribute which is "Kevin"
employeeOne.diff_name()  # Running this function and since the name is "Kevin" it prompts you to change the name
print("Your name is", employeeOne.name)  # Prints out new name
employeeOne.diff_name()  # Prints out last print inside of "else"
