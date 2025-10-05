# print("hello")
# a = 6
# print(a)
# print(a+4)

# print(2>=2)
# print(2!=1)
# print(6>3)
# print('Mike' == "mike")

# Comparison operators: > < >= <=

# Functions in Python
    # def add(a,b):
    #     return a + b
    # print(add(5,3))
    # sum = add(67,90)

    # print(f'sum = {sum}')
# def userAge(age):
#     if age < 18:
#         return "You're not eligible!!"
#     return "Congratulations!!"
# # print(userAge(17))
# print(userAge(19))

# def studentScore(score):
#     grade = ""
#     if score >= 70 and score <= 100:
#         grade = "A"
#     elif score <= 60:
#         grade = "B"
#     elif score <= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade
# stdGrade = studentScore(80)

# prefix = ""

# if stdGrade=="A":
#     prefix = "an"
# print("You scored " + prefix + " " + stdGrade)

# A town has a unique traffic rule. Based on your speed and whether if it's your birthday, the fine varies.
#   Speed <= 60km/h; Not Birthday = No fine; Birthday = No fine
#   Speed 61 - 80km/h; Not BDay = Small fine; BDay = No fine
#   Speed > 80km/h; Not Birthday = Big fine; Birthday = Small fine

def userSpeed(speed, birthday):
    fine = ""
    birthday == True
    
    if speed <= 60 :
        fine = "No Fine"
    elif speed >= 61 and speed <= 80:
        fine = "Small Fine"
    elif speed > 80:
        fine = "Big fine"
    return fine

trafficFine = userSpeed(61,True)
print(trafficFine)