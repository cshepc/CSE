# Defining Functions


def hello_world():
    print('Hello world!')


# hello_world()


def square_it(number):
    return number**2


# print(square_it(3))


def tip_calc(bill):
    tax_amt = bill * 0.18
    total_bill = tax_amt + bill
    return total_bill


# print('Your bill is $%d' % tip_calc(100))


def distance_calc(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


# print(distance_calc(0, 0, 3, 4,))


def pythagorean_calc(a, b):
    first = a ** 2
    second = b ** 2
    third = first + second
    c = third ** 0.5
    return c


print(pythagorean_calc(4, 4))
