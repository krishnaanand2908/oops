class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithharry.com"
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    def printemail(self):
        return self.email
    
    @property
    def cmail(self):
        if self.fname == None or self.lname == None:
            return "**Email is not set. Please set an email**"
        else:
            return f"{self.fname}.{self.lname}@codewithharry.com"
    
    @cmail.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        
    @cmail.deleter
    def cmail(self):
        self.fname = None
        self.lname = None
        
skillf = Employee("Skill", "F")
# print(skillf.cmail)
# print(dir(skillf))

# import inspect
# print(inspect.getmembers(skillf))