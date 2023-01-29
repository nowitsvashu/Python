class Employee:
    increment = 1.5
    no_of_employees =0
    def __init__(self,name,age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary=int(self.salary * Employee.increment)


print(Employee.no_of_employees)
vashu= Employee("vashu",21,100000)
print(Employee.no_of_employees)
print(vashu.salary)
vashu.increase() 
vashu.increment=9
print(vashu.salary)
print(vashu.__dict__)
print(Employee.__dict__)