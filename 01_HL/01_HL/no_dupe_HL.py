already_guessed =[]

secret_num = 7
guesses_used = 0
guesses_allowed = 5


#set guesses
guess = ""
while guess != secret_num:
    guess = int(input("guess: "))

    #check no dupe
    if guess in already_guessed:
        print(f"you hve already guessed {guess}. youve still used "
              f"{guesses_used} / {guesses_allowed}")
        continue

    # if guess not dupe
    else:
        already_guessed.append(guess)

    guesses_used += 1