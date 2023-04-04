#name: Mohammed Sajid
#matrikulation number: 3171311

# import random module
import random

# define the function guess_the_number
def guess_the_number():
    # generate a random number between 1 and 100 and store it in the variable unknown_number
    unknown_number = random.randint(1, 100)
    # initialize the number of guesses to 0
    num_guesses = 0
    # start a loop that runs until the user guesses the number or quits the game
    while True:
        # remind the user to enter their guess or press q to quit
        user_input = input("Guess the number (between 1 and 100), or press q to quit: ")
        # check if the user entered q, if so end the game and print a message
        if user_input == "q":
            print("You quit the Game.")
            return
        # convert the user's input to an integer
        user_guess = int(user_input)
        # increment the number of guesses
        num_guesses = num_guesses + 1
        # check if the user's guess matches the unknown number
        if user_guess == unknown_number:
            # print a congratulatory message with the number of guesses made and end the game
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            return
        # if the user's guess is lower than the unknown number, remind them to try again with a higher guess
        elif user_guess < unknown_number:
            print("Your guess was too low. Try again.")
        # if the user's guess is higher than the unknown number, remind them to try again with a lower guess
        else:
            print("Your guess was too high. Try again.")

# call the guess_the_number function to start
guess_the_number()
