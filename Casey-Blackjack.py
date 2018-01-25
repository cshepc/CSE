import random

deck = {'Ace of hearts': 1, 'Ace of spades': 1, 'Ace of diamonds': 1, 'Ace of clubs': 1}

for card in range(1, 10):
    deck['%i of hearts' % (card + 1)] = card + 1
    deck['%i of spades' % (card + 1)] = card + 1
    deck['%i of diamonds' % (card + 1)] = card + 1
    deck['%i of clubs' % (card + 1)] = card + 1

deck['Jack of hearts'] = 10
deck['Jack of spades'] = 10
deck['Jack of diamonds'] = 10
deck['Jack of clubs'] = 10
deck['Queen of hearts'] = 10
deck['Queen of spades'] = 10
deck['Queen of diamonds'] = 10
deck['Queen of clubs'] = 10
deck['King of hearts'] = 10
deck['King of spades'] = 10
deck['King of diamonds'] = 10
deck['King of clubs'] = 10
print(deck)
