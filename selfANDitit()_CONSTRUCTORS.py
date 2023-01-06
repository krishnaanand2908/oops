class Employee:
    no_of_leaves = 8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and role is {self.role}"
    
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(rohan.printdetails())
# print(harry.printdetails())

print(harry.salary)