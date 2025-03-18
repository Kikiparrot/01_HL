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

    #number between low and high
    else:
        error = ("please enter an integer that"
                 f"if between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        #exit code
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

# Main routine

print()
print("WELCOME TO THE HIGHER LOWER GAME")
print()

# check if user wants instructions
want_instructions = string_checker("do you want to see the instructions?")
if want_instructions == "yes":
    instruction()

# initialise game variables
mode ="regular"
rounds_played = 0

# instructions

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

     # Rounds Heading
    if mode == "infinite":
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} (infinite mode) 🌛🌛🌛"
    else:
        rounds_heading = f"\n🌜🌜🌜 Round {rounds_played + 1} of {num_rounds} 🌛🌛🌛"

    print(rounds_heading)
    print()

    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / stats


























