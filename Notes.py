# print("Hello world")
#
# # casey
#
# a = 4
# b = 3
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



# Functions


def print_hw():
    print("Hello World.")
    print("Enjoy the day.")


print_hw()


def say_hi(name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Casey")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("casey", 15)


def algebra_hw(x):
    return x ** 3 + 4 ** 2 + 7 * x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(90))

'''Write a function that prints out
"sings" (prints) Happy birthday

It must take one parameter called "name"'''


def happy_bday(name):
    print("Happy birthday to you,")
    print("Happy birthday to you,")
    print("Happy birthday dear " + name)
    print("Happy birthday to you.")


happy_bday("Casey")

# Loops

for num in range(10):
      print(num + 1)

      # While Loops (BEWARE!!!!!!)


a = 1
while a < 10:

    print(a)
    a += 1

# Random numbers
import random # This should be on line 1
print(random.randint(0,10))
