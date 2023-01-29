class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, salary)



vashu = Employee.from_str("Vashu-Sharma-400000")


print(vashu.fname)
print(vashu.lname)
print(vashu.salary)
