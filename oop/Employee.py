class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee name: {self.name}")
        print(f"Salary: {self.salary}")