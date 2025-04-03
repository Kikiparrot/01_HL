import random


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


# guess loop



# para

low_num = 0
high_num = 10
guesses_allowed = 5

secret_num = random.randint(low_num, high_num)
# set guesses
guesses_used = 0
already_guessed = []

guess = ""
while guess != secret_num and guesses_used < guesses_allowed:
    guess = int(input("guess: "))

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
        print("too low, please try a higher number \n"
                    f"you have used {guesses_used} out of {guesses_allowed} guesses")


    elif guess > secret_num and guesses_used < guesses_allowed:
        print(f"too high, please try a lower number \n"
                    f"you have used {guesses_used} out of {guesses_allowed} guesses")

    if guess is secret_num:
        print(f"you have got the secret number in {guesses_used} out of {guesses_allowed} guesses! \n")
        end_game = "yes"

    elif guesses_used == guesses_allowed and guess is not secret_num:
        print(" uh oh! you lost :[")

    # special mentions
    if guesses_used == 1 and guess == secret_num:
        print("what a lucky duck! you got the secret number first try!")

    elif guesses_used == 5 and guess == secret_num:
        print("you got the secret number by the skin of your teeth!")

    if guesses_used == 4 and guess is not secret_num:
        print("careful!!! time is running out!")

