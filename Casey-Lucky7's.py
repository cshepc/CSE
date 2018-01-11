import random

balance = 15
top_balance = 15
number_of_turns = 0
top_turn = 0
while balance > 0:
    number_of_turns += 1
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    if die_1 + die_2 == 7:
        balance += 5
        if balance > top_balance:
            top_balance = balance
            top_turn = number_of_turns
    else:
        balance -= 1


print('You started with 15 dollars. It took %s turns for you to run out of money' % number_of_turns)
print('Your top balance was ' + str(top_balance) + ' dollars in round number ' +  str(top_turn))
