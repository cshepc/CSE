import random
import string
'''
This is a guide of how to make hangman

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. hide and reveal letters
5. Create the win condition
'''

word_bank = ["tortoise"]
# , "antidisestablishmentarianism", "hungry", "forgiveness", "inconsolable", "cataclysmic",
#          "euphoria", "perjury", "melancholy", "photosynthetic"]
guesses_left = 10

current_word = random.choice(word_bank)
print(current_word)
current_word = list(current_word)
print(current_word)


guesses = []
output = []

guesses.append(input("Guess a letter. >_"))
for letter in current_word:
    if letter in guesses:
        output.append(guesses)
    else:
        output.append("*")

    print(output)

