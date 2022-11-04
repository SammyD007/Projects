""" Number Guessing Game
----------------------------------------
"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 1000))
    print("'Sup! This is a number guessing game")
    player_name = input("What is your name? ")
    wanna_play = input("'Sup, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    # Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 1000 ")
            if int(guess) < 1 or int(guess) > 1000:
                raise ValueError("Between 1 and 1000, ffs.")
            if int(guess) == random_number:
                print("Yeah thats it.")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts, git gud".format(attempts))
                play_again = input("Another go? Or you too chicken? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 1000))
                if play_again.lower() == "no":
                    print("Fine, leave just like everyone else important in my life.")
                    break
            elif int(guess) > random_number:
                print("Nah, lower")
                attempts += 1
            elif int(guess) < random_number:
                print("Nah, higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
    
