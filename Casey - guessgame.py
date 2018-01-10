import random

# Initializing variables
correct_guess = False
rand_int = random.randint(0, 50)
guesses = 5

# Describes ONE turn (This is the game's Controller)
while correct_guess is False and guesses > 0:
    player_guess = input("Guess a number between 0 and 50")
    player_guess = int(player_guess)
    if rand_int == player_guess:
        print("Yay!")
        correct_guess = True
    elif player_guess > rand_int:
        print("Too high!")
        guesses = guesses - 1
    elif player_guess < rand_int:
        print("Too low!")
        guesses = guesses - 1
