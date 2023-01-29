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
        if day=="sunday":
            return True
        else:
            return False

    
    def __add__(self, other):
        return self.salary+ other.salary

    def __repr__(self):
        return 'Employee({0},{1},{2})'.format(self.fname, self.salary, self.lname)

vashu = Employee.from_str("Vashu-Sharma-400000")
vanshika = Employee.from_str("Vanshi- Aggarwal-800000")
print(repr(vanshika))