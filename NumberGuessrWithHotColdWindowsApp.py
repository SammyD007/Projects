""" Number Guessing Game
----------------------------------------
"""
import random
import tkinter as tk
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 500)
canvas1.pack()
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 1000))
    labeln = tk.Label(root, text= 'Sup, this is a number guessing game.', fg='green', font=('helvetica', 12, 'bold'))
    canvasl.create_window(150, 200, window=labeln)
    player_name = input('What is your name?')
    wanna_play = input("'Sup, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    # Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input(tk.Label(root, text="Pick a number between 1 and 1000 ", fg='green', font=('helvetica', 12, 'bold'))
            if int(guess) < 1 or int(guess) > 1000:
                raise ValueError(tk.Label(root, text="Between 1 and 1000, ffs.", fg='green', font=('helvetica', 12, 'bold'))
            if int(guess) == random_number:
                print(tk.Label(root, text="Yeah thats it.", fg='green', font=('helvetica', 12, 'bold'))
                attempts += 1
                attempts_list.append(attempts)
                if attempts > 15:
                    print("You are pretty trash, ngl")
                else:
                    print("It took you {} attempts, git gud".format(attempts))
                play_again = input("Another go? Or you too chicken? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 1000))
                if play_again.lower() == "no":
                    print("Fine, leave just like everyone else important in my life.")
                    break
            elif int(guess) > random_number:
                if (int(guess) - int(random_number)) < 10:
                    print("Closer, still too high, nerd")
                else:
                    print("Nah, lower")
                attempts += 1
            elif int(guess) < random_number:
                if (int(random_number) - int(guess)) < 10:
                    print("Closer, still too low, nerd")
                else:
                    print("Nah, higher")
                attempts += 1
        except ValueError as err:
            print("Put in a number in the value range. ffs...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    
    root.mainloop()
    start_game()
    
