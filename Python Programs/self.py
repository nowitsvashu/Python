class Employee:

    def print_name(self):
        return f"The name is {self.name} and age is {self.age}."

vashu=Employee()

vashu.name="vashu"
vashu.age="21"

print(vashu.print_name())