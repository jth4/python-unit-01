# numberGuessingGame.py
import random

def start_game():
    print(">>>>> WELCOME TO THE GUESSING GAME! <<<<<")
    print("The computer has generated a random number from 1-10.  Try to guess it!")

    random_num = random.randint(1, 10)
    # print(random_num)

    player_guess = int(input("Your guess: "))

    counter = 1
    while player_guess != random_num:
        if player_guess < random_num:
            counter += 1
            is_higher = "Higher!"
            print(is_higher)
            player_guess = int(input("Your guess: "))
        elif player_guess > random_num:
            counter += 1
            is_lower = "Lower!"
            print(is_lower)
            player_guess = int(input("Your guess: "))

    print("You got it in {} attempts".format(counter))
    print("Game over!")

start_game()