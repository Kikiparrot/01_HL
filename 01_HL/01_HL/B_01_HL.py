import math
import random


# Check that users have entered a valid answer
def string_checker(question, valid_ans=("yes", "no")):
    error = f"please enter a valid option from the following list: {valid_ans}"
    while True:
        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as
            # the first letter of an item in the alphabet
            elif user_response == item[0]:
                return item

        # print out error if user does not enter something 'valid'
        print(error)
        print()

def yes_no(question):
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")

def instruction():
    """prints instructions"""

    print("""
    *** Instructions ***

    To begin, choose the number of rounds and either customize the game
    parameters or go with the default game (where the secret number will 
    be between 1 and 100)

    Then choose how many rounds you would like to play or <enter> 
    for infinite mode

    Your goal is to try and guess the secret number without running out
    of guesses
     Have Fun !!
         """)


def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed
    if low is None and high is None:
        error = "please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = ("please enter an integer that is "
                 f"more than / equal to {low}")

    # number between low and high
    else:
        error = ("please enter an integer that"
                 f"if between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        # exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # integer is not too low
            if low is not None and response < low:
                print(error)
            # response is more than low number
            elif high is not None and response > high:
                print(error)
            # valid response
            else:
                return response

            # if response valid, return it
            return response

        except ValueError:
            print(error)


# calc num of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main routine

print()
print("WELCOME TO THE HIGHER LOWER GAME")
print()

# check if user wants instructions
want_instructions = string_checker("do you want to see the instructions?")
if want_instructions == "yes":
    instruction()

# initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []
# instructions

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? push <enter> for infinite mode: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

default_params = yes_no("do you want to use the default parameters? ")
if default_params == "yes":
    low_num = 1
    high_num = 10
    guesses_allowed = 5

else:
    low_num = int_check("low number? ")
    high_num = int_check("high number? ", low=low_num + 1)
    guesses_allowed = 5

# game loop starts here
while rounds_played < num_rounds:
    # generate secret number
    # random integer between low_num and high_num

    # Rounds Heading
    if mode == "infinite":
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} (infinite mode) 🌛🌛🌛"
        num_rounds += 1
    else:
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} of {num_rounds} 🌛🌛🌛"

    rounds_played += 1
    print(rounds_heading)
    print()

    user_choice = f"choose: a number between {low_num} and {high_num}"


    guesses_used = 0
    already_guessed = []
    secret_num = random.randint(low_num, high_num)

    guess = ""
    while guess != secret_num and guesses_used < guesses_allowed:
        guess = int_check("guess: ", low_num, high_num, "xxx")

        if guess == "xxx":
            end_game = "yes"
            break

        # check no dupe
        elif guess in already_guessed:
            print(f"you hve already guessed {guess}. youve still used "
                        f"{guesses_used} / {guesses_allowed}")
            continue

        # if guess not dupe
        else:
            already_guessed.append(guess)

        guesses_used += 1

        if guess < secret_num and guesses_used < guesses_allowed:
            feedback = ("too low, please try a higher number \n"
                        f"you have used {guesses_used} out of {guesses_allowed} guesses")


        elif guess > secret_num and guesses_used < guesses_allowed:
            feedback = (f"too high, please try a lower number \n"
                        f"you have used {guesses_used} out of {guesses_allowed} guesses")

        if guess is secret_num:
            feedback = (f"you have got the secret number in {guesses_used} out of {guesses_allowed} guesses! \n")


        elif guesses_used == guesses_allowed and guess is not secret_num:
            feedback = " uh oh! you lost :["

        # special mentions
        if guesses_used == 1 and guess == secret_num:
            feedback = "what a lucky duck! you got the secret number first try!"

        elif guesses_used == 5 and guess == secret_num:
            feedback = "you got the secret number by the skin of your teeth!"

        if guesses_used == 4 and guess is not secret_num:
            feedback = "careful!!! time is running out!"


    # print feedback
        print(feedback)

    # game history / stats
