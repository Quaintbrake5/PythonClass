from Employee import Employees

class Developer(Employees):
    def __init__ (self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
        
    def show_details(self):
        return super().show_details()
        print(f"Programming Language: {self.language}")