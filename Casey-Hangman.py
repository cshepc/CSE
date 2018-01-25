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

word_bank = ["tortoise", "antidisestablishmentarianism", "hungry", "forgiveness", "inconsolable", "cataclysmic",
             "euphoria", "perjury", "melancholy", "photosynthetic"]
def hangman():
    play_again = True
    user_choice = ''
    while play_again is True:
        guesses_left = 10
        current_word = random.choice(word_bank)
        # print(current_word)
        print("*" * len(current_word))
        list_word = list(current_word)


        guesses = []
        print("Your word has %i letters in it" % len(current_word))
        while guesses_left > 0:
            current_guess = input("Guess a letter. >_")
            guesses.append(current_guess)

            output = []
            if current_guess not in list_word:
                guesses_left -= 1
            print("You have %s guesses left" % guesses_left)
            for letter in list_word:
                if current_guess == "stop":
                    exit(0)
                if letter in guesses:
                    output.append(letter)
                else:
                    output.append("*")
            output = ''.join(output)
            if "*" not in output:
                print("You win! the word you found was %s" % current_word)
                user_choice = input("Play again? (y/n) >_")
                if user_choice == "yes" or "y":
                    print("\n\n\n")
                    return
                else:
                    exit(0)
        print("You lose! The word was %s" % current_word)


hangman()

