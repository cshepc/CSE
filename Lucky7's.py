import random
balance = 15
number_of_turns = 0
while balance > 0:
    number_of_turns += 1
    #print("turn %s" % number_of_turns)
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    if die_1 + die_2 == 7:
        balance += 5
    else:
        balance -= 1


print("You started with 15 dollars. It took %s turns for you to run out of money" % number_of_turns)
