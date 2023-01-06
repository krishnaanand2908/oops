class Employee:
    no_of_leaves = 8

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

Employee.no_of_leaves = 9
print(Employee.no_of_leaves)

rohan.no_of_leaves = 10
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

print(rohan.__dict__)

# print(no_of_leaves)
print(Employee.__dict__)
