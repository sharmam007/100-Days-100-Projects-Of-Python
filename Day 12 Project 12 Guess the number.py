#!/usr/bin/env python
# coding: utf-8

# In[1]:


logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! the answer was {actual_answer}")

def set_difficulty():
    level =  input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Moh's number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer} ")


    turns = set_difficulty()

    guess = 0


    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\n"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()


# In[ ]:




