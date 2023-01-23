# GuessingGame.py
# @ Author: K A Warmington
# Date: 18.12.2022

number_of_tries = 4
# secret number = 17

print("Welcome to the guessing game, try to guess the number in 4 attempts")

while True:
    answer = input("What is your guess?...\n")
    if answer == "17":
        print("Correct! Well done!\n")
        # correct answer, so exit loop using break
        break
    elif answer > "17":
        print("Sorry that is the wrong answer, the secret number is lower."
              "Try again!\n")
        number_of_tries -= 1
    elif answer < "17":
        print("Sorry that is the wrong answer, the secret number is higher."
              "Try again!\n")
        number_of_tries -= 1

    # check number of tries and break if none left
    if number_of_tries == 0:
        print("You have run out of goes. Sorry!")
        break

x = input("Press any key to exit.")
        
