# '''
#
# '''
# print("Hello world")
#
# # casey
#
# a = 4
# b = 3
# print("Hello world")
#
# # casey
#
# print(3+5)
# print(5-3)
# print(3*5)
# print(6/2)
# print(3 ** 2)
#
# print("try to figure out how this works")
# print(11 % 5)
#
# # the "%" sign is a modulus. It finds a remainder.
#
# car_name = " the casey mobile"
# car_type = "Volkswagen"
# car_cylinders = 10
# car_mpg = 6000
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s."% (car_name, car_type)) #watch the order
#
# # here is where we get a little fancy
# print("What is your name?")
# name = input(">_")
# print("Hi %s." %name)
#
# age = input("How old are you?")
# print("%s?! That's really old. You belong in a Chilis." %age)
#
#
#
# # Functions
#
#
# def print_hw():
#     print("Hello World.")
#     print("Enjoy the day.")
#
#
# print_hw()
#
#
# def say_hi(name):  # Name is a "parameter"
#     print("Hello %s" % name)
#     print("Coding is great!")
#
#
# say_hi("Casey")
#
#
# def print_age(name, age):
#     print("%s is %d years old" % (name, age))
#     age += 1  # age = age + 1
#     print("Next year, %s will be %d years old" % (name, age))
#
#
# print_age("casey", 15)
#
#
# def algebra_hw(x):
#     return x ** 3 + 4 ** 2 + 7 * x - 4
#
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# # if statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc(90))
#
# '''Write a function that prints out
# "sings" (prints) Happy birthday
#
# It must take one parameter called "name"'''
#
#
# def happy_bday(name):
#     print("Happy birthday to you,")
#     print("Happy birthday to you,")
#     print("Happy birthday dear " + name)
#     print("Happy birthday to you.")
#
#
# happy_bday("Casey")
#
# # Loops
#
# for num in range(10):
#       print(num + 1)
#
#       # While Loops (BEWARE!!!!!!)
#
#
# a = 1
# while a < 10:
#
#     print(a)
#     a += 1
#
# # Random numbers
# import random  # This should be on line 1
# print(random.randint(0,10))
#
#
# # Recasting
# c = '1'
# print(c == 1)  # we have a string and an integer
# print(int(c) == 1)
# print(c == str(1))
#
#
# # Comparisons
#
# print(1 == 1)  # Use a double equal sign
# print(1 != 2)  # 1 is not equal to 2
# print(not False)  # "!" is the "not" operator
#
# Lists
#
# the_count = [1, 2, 3, 4, 5]
# cheeseburger_ingredients = ['cheese', "🅱eef", 'sauce', 'sesame seed bun', 'avocado', 'onion']
# print(cheeseburger_ingredients[0])
# print(len(cheeseburger_ingredients))
#
# # Going through lists
# for generic_item_name in cheeseburger_ingredients:
#     print(generic_item_name)
#
# for h in the_count:
#     print(h * 2)
#
# length = len(cheeseburger_ingredients)
# range(5)  # A list of the numbers 0 through 4
# range(len(cheeseburger_ingredients))  # Generates a list of all indices
#
# for num in range(len(cheeseburger_ingredients)):
#     item = cheeseburger_ingredients[num]
#     print("The item at index %d is %s" % (num, item))
#
# # Recasting into a list
#
# strOne = "Hello World!"
# listOne = list(strOne)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# print(listOne[-1])
#
#
# # Adding things to a list
# cheeseburger_ingredients.append("Fries")
# print(cheeseburger_ingredients)
# cheeseburger_ingredients.append("teeth")
#
# # Removing things from a list
# cheeseburger_ingredients.pop(1)
# print(cheeseburger_ingredients)
# cheeseburger_ingredients.remove("cheese")
# print(cheeseburger_ingredients)
#
# # Getting the alphabet
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)
#
#
# # Making things lowercase
# strTwo = "ThIs Is A VeRy oDd sEnTeNce"
# lowercase = strTwo.lower()
# print(lowercase)

# Dictionaries - Made up of key: value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary
print(dictionary["name"])
print(dictionary['age'])
print(dictionary['height'])

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'San Francisco',
        'San Jose'
    ],
    'AZ': [
        'Phoenix',
        'Tuscon'
    ],
    'NY': [
        'New York City',
        'Brooklyn'
    ],
}

print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])
