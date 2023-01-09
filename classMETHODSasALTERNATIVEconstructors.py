class Employee:
    no_of_leaves = 8
    
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"The name is {self.name}. The salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
        
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
    
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")
karan = Employee.from_dash("Karan-480-Student")

harry.change_leaves(10)

# print(harry.no_of_leaves)
print(karan.salary)