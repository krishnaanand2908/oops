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
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)
        
class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages
        
    def printprog(self):
        return f"Programmer's name is {self.name}. The salary is {self.salary}, role is {self.role} and "

    
    
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")
# karan = Employee.from_dash("Karan-480-Student")
shubham = Programmer.from_dash("Shubham-555-Programmer-['python']")
karan= Programmer.from_dash("Karan-777-Programmer-['python']")

# harry.printgood('but kinda torturing.')
print(karan.printprog())