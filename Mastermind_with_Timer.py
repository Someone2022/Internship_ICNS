# Mastermind with timer
# in this game the computer generates 4 random digits between 1 and 6 and the user has to guess the values and their
# order. Computer in response returns some feedback as follows:
# - B if the digit and its position are correct,
# - W if the digit is correct, but its position is wrong,
# - G if the digit is wrong.
# different from the simple version (found in Mastermind.py) here the user can decide whether he/she wants to play
# with or without the timer with a pre-set time limit. Here it is set on 4 minutes, but one can change it by setting
# variable, t (see line 43)
# Input: number of digits: num_digits, user guess at each turn: user_guess, and maximum number of allowed guesses:
# max_guesses
# Output: "B, W, G", "you win/ lose", "your time is over"
# Author: someone
# Date: 21.01.2022

# import required functions and packages
import random
import time


# my functions
# this function checks all the indices and returns a flag for each index
def digits(num_digits, random_digits, user_guess):
    for j in range(0, num_digits):
        if user_guess[j] == random_digits[j]:
            yield "B"
        elif random_digits.count(user_guess[j]) == 1:
            yield "W"
        else:
            yield "G"


# this function converts a list of digits to the same list of strings
def listToString(x):
    str1 = " "
    return (str1.join(x))


# defining values
initial_set = [1, 2, 3, 4, 5, 6]
random_digits = list(random.sample(initial_set, 4))
max_guesses = 7
num_digits = 4
t = 240  # time is in seconds

# print the instruction
print("*** Welcome to Mastermind ***")
print("Do you want to start? (Y/N)")
user_want_play = input()
if user_want_play == "n" or user_want_play == "N":
    pass
else:
    print("Do you want to play with(w) or without(wo) timer?")
    user_want_timer = input()
    if user_want_timer == "wo":
        print("The computer has generated a", num_digits, "digits secret code and you have",
              max_guesses, "guesses to find it.", "\n", "Enter", num_digits, "digits between 1 and 6 with spaces."
              " (Digits repetition is not allowed.)", "\n", "Guess N:XXXX", "\n", "B = Correct digits in correct place",
              "\n", "W = Correct digits but in wrong places", "\n", "G = Wrong digit", "\n",
              "-------------------------------------")
        # Guess 1
        for i in range(1, max_guesses+2):
            if i == max_guesses+1:
                print("Sorry you have lost. The secret code was:", random_digits, ".")
                break
            print("Guess Number %s:" % (i))
            user_guess = list(map(int, list(input().split())))
            if user_guess == random_digits:
                print("You found the secret code in", i, "turns!")
                break
            # Guess 2 and further
            else:
                feedback = list(map(str, digits(num_digits, random_digits, user_guess)))

                # optimization of depiction
                for idx in range(0, num_digits):
                    if feedback[idx] == "G":
                        feedback.append(feedback.pop(feedback.index("G")))
                    elif feedback[idx] == "B":
                        feedback.insert(0, feedback.pop(idx))

                print(listToString(feedback[:round(num_digits / 2)]))
                print(listToString(feedback[round(num_digits / 2):num_digits]))


    else:
        start = time.time()
        print("The computer has generated a", num_digits, "digits secret code and you have",
              max_guesses, "guesses to find it.", "\n", "Enter", num_digits, "digits between 1 and 6 with spaces."
              " (Digits repetition is not allowed.)", "\n", "Guess N:XXXX", "\n", "B = Correct digits in correct place",
              "\n", "W = Correct digits but in wrong places", "\n", "G = Wrong digit", "\n",
              "-------------------------------------")
        # Guess 1
        for i in range(1, max_guesses + 2):
            end = time.time()
            if (end - start) < t:
                if i == max_guesses + 1:
                    print("Sorry you have lost. The secret code was:", random_digits, ".")
                    break
                print("Guess Number %s:" % (i))
                user_guess = list(map(int, list(input().split())))
                if user_guess == random_digits:
                    print("You found the secret code in", i, "turns!")
                    break
                # Guess 2
                else:
                    feedback = list(map(str, digits(num_digits, random_digits, user_guess)))

                    # optimization of depiction
                    for idx in range(0, num_digits):
                        if feedback[idx] == "G":
                            feedback.append(feedback.pop(feedback.index("G")))
                        elif feedback[idx] == "B":
                            feedback.insert(0, feedback.pop(idx))

                    print(listToString(feedback[:round(num_digits / 2)]))
                    print(listToString(feedback[round(num_digits / 2):num_digits]))

            else:
                print("Sorry, your time is over.")
                break
