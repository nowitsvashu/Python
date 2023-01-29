class Employee:
    salary=700
    pass

vashu=Employee()
xyz=Employee()

vashu.name="vashu"


print(vashu.name)
print(vashu.salary)

Employee.salary=10
print(vashu.salary)

vashu.salary=1
print(vashu.__dict__)
print(Employee.salary)
print(vashu.salary)
print(Employee.__dict__)