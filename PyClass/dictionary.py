car = {
    'brand': "Dodge",
    'model': "Charger",
    'trim': "SRT Hellcat",
    'year': 2020,
    'transmission': "Dual Clutch",
    'colors': ['red', 'blue', 'red with black stripes', 'matte black']
}
# print(car)
# print(type(car))
# print(len(car))

# get a single value
# print(car.get('trim'))

# get all keys
# print(car.keys())
# ky = car.keys()
# print(ky)

car["tinted"] = ['aftermarket', 'grade 0', 'grade 1']
# print(car)

# Retrieving all car values
car_values = car.values()
# print(car_values)

# Retrieve all car items
# print(car.items())

# 
# if 'year' in car:
#     car['year'] = 2035
    
# print(car)

# Remove from dictionary
car.pop('model')
# del car['model']
# print(car)
# del car
# print(car)

# for x in car:
#     if x.startswith('b'):
#        result =  x.upper()
#     print(result)

# for value in car.values():
# print(value)

# for key in car.keys():
#     print(key)

# myCopy = car.copy()
# print(myCopy)

# myCopy = dict(car)
# print(myCopy)

user1 = {
    "name": "Maria",
    'gender': 'female'
}

user2 = {
    'name': 'Anais',
    'gender': 'female'
}

user3 = {
    'name': 'Mark',
    'gender': 'male'        
}

users = {
    'first': user1,
    'second': user2,
    'third': user3
}
# print(users)
print(users['first']['skills'][-1])
