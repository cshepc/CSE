import random

ace = 1
jack = 10
queen = 10
king = 10

deck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
suits = ["diamonds", "hearts", "spades", "clubs"]
suits = suits * 13
deck = deck * 4
card1 = random.choice(deck)

suit1 = random.choice(suits)

print(card1)
print(suit1)

meme = []

for card in range(0, 52):



if card1 == deck[ace]:
    print("Ace of %s" % suit1)
    suits.remove(suit1)
    deck.remove(card1)
    print(len(suits))
    print(len(deck))
elif card1 == deck[jack]:
    print("Jack of %s" % suit1)
    suits.remove(suit1)
    deck.remove(card1)
    print(len(suits))
    print(len(deck))
elif card1 == deck[queen]:
    print("Queen of %s" % suit1)
    suits.remove(suit1)
    deck.remove(card1)
    print(len(suits))
    print(len(deck))
elif card1 == deck[king]:
    print("King of %s" % suit1)
    suits.remove(suit1)
    deck.remove(card1)
    print(len(suits))
    print(len(deck))
else:
    print("%i of %s" % (card1, suit1))
    suits.remove(suit1)
    deck.remove(card1)
    print(len(suits))
    print(len(deck))
