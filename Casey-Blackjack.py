import random

deck = []

for card in range(0, 13):
    card1 = card + 1
    # print(card1)
    suit1 = "Diamonds"
    # print(suit1)
    set1 = [card1, suit1]
    deck.append(set1)

    card2 = card + 1
    # print(card2)
    suit2 = "Hearts"
    # print(suit2)
    set2 = [card2, suit2]
    deck.append(set2)

    card3 = card + 1
    # print(card3)
    suit3 = "Spades"
    # print(suit3)
    set3 = [card3, suit3]
    deck.append(set3)

    card4 = card + 1
    # print(card4)
    suit4 = "Clubs"
    # print(suit4)
    set4 = [card4, suit4]
    deck.append(set4)

    # print(deck)

callDeck = deck
# print(callDeck)
flat_deck = [item for sublist in callDeck for item in sublist]
# print(flat_deck)
flat_deck[0] = "Ace"

for num in range(0, 26):

    if flat_deck[num + 1 * 2 - 1] == 1:
        flat_deck[num + 1 * 2 - 1] = "Ace"

    elif flat_deck[num + 1 * 2 - 1] == 11:
        flat_deck[num + 1 * 2 - 1] = "Jack"

    elif flat_deck[num + 1 * 2 - 1] == 12:
        flat_deck[num + 1 * 2 - 1] = "Queen"

    elif flat_deck[num + 1 * 2 - 1] == 13:
        flat_deck[num + 1 * 2 - 1] = "King"

print(flat_deck)