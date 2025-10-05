from Employee import Employees

class Manager(Employees):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        return super().show_details()
        print(f"Department: {self.department}")