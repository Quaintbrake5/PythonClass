# Write on how Pythom memory works in handling string and other data structures

name = 'King'
# print(name[0])

# sentence = """
# This is just a test... This is so cool.... How do you think this works???
# This is great..... OMG....
# OMDS.... Life sucks guys......
# Hello.... Hello gooners XD....
# """
# print(sentence)

school = "Aptech Port Harcourt"
# for x in school:
#     print(x)

# String Length
# print(len(school))

# To check if part of string exist
# if "Port" not in school:
#     print("Be specific!")
# else:
#     print("Doesn't exist!!")

# slicing
message = "This is the message"
# print(message[12:])
# print(message[-5:-2])
# print(message.upper())
# print(message.lower())


msg = "                             hello"
# print(len(msg.strip()))

ex = "Uche, Bimbo, Maria"
# 
newStr = ex.split(",")
# print(type(newStr))
# print(newStr)

# Format String
friend = "Zion"
# print(f"My friend is {friend}")

quantity = 3
unit_price = 400
total_sale = f"Total: {quantity * unit_price}" 
# print(total_sale)

account_number = 'a1234see'
# print(account_number.isalpha())
# print(account_number.isalnum())

# Reverse
def reverseStr(str):
    return str[::-1]
# print(reverseStr("hello"))

# Palindrome checker

def checkPalindrome(str):
    new_str = str.lower()
    return str[::-1] == new_str
print(checkPalindrome("noon"))
