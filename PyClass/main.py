# from module import getUser
import platform
pf = dir(platform)

# print(getUser("Denzyl"))
# pf = platform.system()
# print(pf)
from Manager import Manager
from Developer import Developer

# from rest


emp1 = Manager("Nathan", 5000, "IT")
emp2 = Developer("King", 5300, "HTML")

emp1.show_details()
print("___****___****___")
print()
emp2.show_details