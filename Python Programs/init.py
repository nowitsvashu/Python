class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age

    def print_name(self):
        return f"The name is {self.name} and age is {self.age} and salary is {self.salary}"

    @classmethod
    def from_string(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])


vashu = Employee("vashu", 21, 2100000)
vashu = Employee.from_string("Vashu-4842-6396665246")


print(vashu.age)
