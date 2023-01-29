class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == "sunday":
            return True
        else:
            return False


class Programmer(Employee):
    def __init__(self, fname, lname, salary,proglag,exp):
        super().__init__(fname, lname, salary)
        self.proglag = proglag
        self.exp = exp

    def inc(self):
         self.salary=int(self.salary * self.inc)


vashu = Programmer("Vashu", "Sharma", 199999,"Python","5 Years")
print(vashu.fname)
print(vashu.lname)
print(vashu.salary)
print(vashu.proglag)
print(vashu.exp)

print(vashu.inc())