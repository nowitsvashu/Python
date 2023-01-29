class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + lname + '@gmail.com'
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


if __name__ == '__main__':
    vashu = Employee("vashu","sharma",100000)
    print(vashu.email)