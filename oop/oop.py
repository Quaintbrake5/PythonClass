#  A class is a blueprrint that defines where an object can be created
# OOP (Object Oriented Programming) is a concept of programming that deals with

# Object is an entity of a class. Every object has an attribute and behaviour...

class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def __str__(self):
        return f"Name: {self.firstName} {self.lastName}"
    
    # def user_details(self):
    #     return f"Name: {self.firstName} {self.lastName}"
    
# p1 = Person("Korede", "Zion")
# p1.lastName = "Price"
# print(p1)

class Laptop():
    def __init__(self, serial_Number, brand, model, year):
        self.serial_Number = serial_Number
        self.brand = brand
        self.model = model
        self.year = year
        
    def __str__(self):
        return f"Laptop: {self.serial_Number} {self.brand} {self.model} {self.year}"

l1 = Laptop(1 ,"Apple", "MacBook Air", 2022)
l2 = Laptop(2, "HP", "Elitebook", 2021)
l3 = Laptop(3, "DELL", "Latitude 5410", 2024)
l4 = Laptop(4, "Samsung", "Galaxy Book 5 Pro", 2024)
l5 = Laptop(5, "Infinix", "InBook X1 Pro", 2020)

# laptops = {
#     "first": l1,
#     "second": l2,
#     "third": l3,
#     "fourth": l4,
#     "fifth": l5
# }
# print(laptops)

print(l1, l2, l3, l4, l5)