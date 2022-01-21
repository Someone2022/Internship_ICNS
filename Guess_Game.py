# The Guess Game
# In this game the computer generates a random integer number between 0 and max_value (here 1000) and the user has to
# guess this digit in num_guesses (here 10) turns with the help of the feedbacks he/she gets from the computer.
# Input: number of allowed guesses: num_guesses, maximum value the random digit may have: max_value, and the user guess:
# user_guess which has to be an integer
# Output: "your number is smaller/ bigger", "you win/ lose"
# Author: someone
# Date: 21.01.2022

# import required functions or packages
import random

# defining variables
num_guesses = 10
max_value = 1000

# generate a random variable between 0 and the max_value
rand_num = random.randrange(max_value)

# start
print("Do you want to start?")
usr_want_play = input()
if usr_want_play == "no":
    pass
else:
    print("I have chosen a number between 0 and", max_value, ".",
          "\n", "Can you guess what it is?", "\n", "You have", num_guesses, "guesses...")
    print("Guess Number 1:")
    for i in range(2, (num_guesses + 2)):
        user_guess = int(input())
        if user_guess == rand_num:
            print("Hurrah!!!! You have found it!!!!")
            break
        # Number 2 and further
        elif user_guess < rand_num:
            if i == (num_guesses + 1):
                print("I´m sorry. The correct answer was:", rand_num)
                break
            else:
                print("Your number is smaller.")
                print("Guess Number", i, ":")
        else:
            if i == (num_guesses + 1):
                print("I´m sorry. The correct answer was:", rand_num)
                break
            else:
                print("Your number is bigger.")
                print("Guess Number", i, ":")
