class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __private = 98
    
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
        
class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name}. The game is {self.game}."
    
class CoolProgrammer(Player, Employee):
    # var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)
      
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")
    
shubham = Player("Shubham", ["Cricket"])
karan = CoolProgrammer("Karan", ["Cricket"])

emp = Employee("Harry", 1000, "Clerk")
print(emp._protec)
print(emp._Employee__private)

