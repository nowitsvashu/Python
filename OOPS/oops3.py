class Employee:
    increment = 1.5
    no_of_employees =0
    def __init__(self,name,age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary=int(self.salary * self.increment)
    
    @classmethod
    def change_salary(cls,amount):
        cls.increment=amount




vashu= Employee("vashu",21,100000)

print(vashu.salary)
Employee.change_salary(10)
vashu.increase()
print(vashu.salary)
