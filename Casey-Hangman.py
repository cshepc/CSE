import random
import string

word_bank = ["Tortoise", "Antidisestablishmentarianism", "Hungry", "Forgiveness", "Inconsolable", "Cataclysmic",
             "Euphoria", "Perjury", "Melancholy", "Photosynthetic", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]


def hangman():
    guesses_left = 10
    current_word = random.choice(word_bank)
    current_word = current_word.lower()
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
        print(output)
        if "*" not in output:
            print("You win! the word you found was %s" % current_word)
            user_choice = input("Play again? (y/n) >_")
            if user_choice == "y":
                print("\n\n\n")
                hangman()
            else:
                exit(0)
    print("You lose! The word was %s" % current_word)


hangman()
