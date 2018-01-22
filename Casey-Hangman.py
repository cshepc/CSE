import random
import string
'''
This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Hide the word (use * or _)
4. Reveal Letters based on input
5. Create win and lose conditions
'''

word_bank = ["tortoise", "antidisestablishmentarianism", "hungry", "forgiveness", "inconsolable", "cataclysmic",
             "euphoria", "perjury", "melancholy", "photosynthesis"]

current_word = random.choice(word_bank)
print(current_word)
hidden_word = ""
for word in range(len(current_word)):
    hidden_word += "*"

hidden_word = list(hidden_word)
print(hidden_word)

current_word = list(current_word)
print(current_word)

guess = input("Guess a letter")

if guess in current_word:
    print("h")
else :
    print("Nope! Guess again!")
