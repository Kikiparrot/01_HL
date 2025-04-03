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

# MAIN ROUTINE
print()
print("WELCOME TO THE HIGHER LOWER GAME")
print()


# check if user wants instructions
want_instructions = string_checker("do you want to see the instructions?")
if want_instructions == "yes":
    instruction()

print("program explodes and we all die")
# ask user if they want to see the instructions and display
# them if requested
