#Coin Flip game 

import os
import random

print("Welcome to the game")

def flip_result(guess):
    flip_result = random.choice(["Heads", "Tails"])
    if guess == flip_result:
        print (f"You guessed {guess}. The coin landed on {flip_result}. You won!")
    else:
        print (f"You guessed {guess}. The coin landed on {flip_result}. You lost!")

    
def get_guess():
    guess = input("Heads or Tails: ")
    if guess in ["Heads" , "Tails"]:
        return guess
    else:
        print("Inavlid.Try again!")
        return get_guess()

    
def play_game():
    while True:
        guess = get_guess()
        flip_result(guess)
        again = input(("Do you want to play again? (yes/no) "))
        if again == "no":
            print("Thanks for playing")
            break
play_game()
