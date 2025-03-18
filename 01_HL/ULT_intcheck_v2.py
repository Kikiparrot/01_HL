
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
        error = ("please enter an integer that "
                 f"is between {low} and {high} (inclusive)")
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


# rounds = "test"
# while rounds != "":
    # rounds = int_check("rounds <enter for infinite>: ", low=1, exit_code="")
    # print(f"you asked for {rounds}")

# low_num = int_check("low number? ")
# print(f" you chose a low number of {low_num}")

# high_num = int_check("high number? ", low=1)
# print(f"you chose a high number of {high_num}")

# check guesses
guess = ""
while guess != "xxx":
    guess = int_check("guess: ", low=0, high=10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()