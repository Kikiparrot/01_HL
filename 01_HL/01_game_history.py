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

def int_check(question, low=None, high=None, exit_code=None,):
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



    rounds_won = 0
    rounds_lost = 0

    rounds_won = rounds_played - rounds_lost
    rounds_lost = rounds_played - rounds_won

    while True:
        rounds_played = rounds_won + rounds_lost
        if rounds_played == num_rounds:
            break

        if feedback == "lose":
            rounds_lost += 1

        elif feedback == "won":
            rounds_won += 1




    if num_rounds == rounds_played:

        for item in game_history:
            print(item)
            round_feedback = f"{rounds_played}, {rounds_won} and {rounds_lost}"
            history_item = f"round: {rounds_won} - {rounds_lost}"

            print(round_feedback)
            print("rounds played debugging", rounds_played)

        print()
        print(" ❌❌❌ GAME OVER ❌❌❌ ")
        # calculate stats

        see_history = string_checker(" \ndo you want to see your game history?")
        if see_history == "yes":
            for item in game_history:
                print(item)

        game_results = f"{rounds_played}: Rounds won: {rounds_won}| " \
                       f"rounds lost {rounds_lost},"

        print(game_results)
        game_history.append(game_results)

        # output game stats
        print("+++ game statistics +++")
        print(f"{rounds_won}, {rounds_lost}")

        print()
        print("thanks for playing ")

    elif user_choice == "xxx":
        print()
        print(" ❌❌❌ GAME OVER ❌❌❌ ")
        print("u quit")


# initialise list to hold game history
#game_history = []
#feedback = ""
# get data (base component does this automatically, code below for testing purposes?
#rounds_won = 0
#rounds_lost = 0
#rounds_played = int(rounds_won + rounds_lost)
#round_feedback = rounds_played
#while True:
    #rounds_played = f"you have played {rounds_played} rounds"
    #if rounds_played == "":
   #     break

  #  if feedback == "lose":
 #       rounds_lost += 1

#    elif feedback == "won":
    #    rounds_won += 1

   # rounds_won = int(f"{rounds_won}")
  #  rounds_lost = int(f"{rounds_lost} ")
 #   rounds_played = int(f"{round_feedback}")

#    game_results = f"{rounds_played}: Rounds won: {rounds_won}| " \
     #              f"rounds lost {rounds_lost},"

    #print(game_results)
    #game_history.append(game_results)


   # for item in game_history:
   #     print(item)
    #    round_feedback = f"{rounds_played}, {rounds_won} and {rounds_lost}"
     #   history_item = f"round: {rounds_won} - {rounds_lost}"

  #      print(round_feedback)
 #       print("rounds played debugging", rounds_played)

#    if len(game_history) > 0:
       # print()
      #  print(" ❌❌❌ GAME OVER ❌❌❌ ")
     #   # calculate stats
    #    rounds_won = rounds_played - rounds_lost
   #     percent_won = rounds_won / rounds_played * 100
  #      percent_lost = rounds_lost / rounds_played * 100


        #see_history = string_checker(" \ndo you want to see your game history?")
       # if see_history == "yes":
      #      for item in game_history:
     #           print(item)

    #    # output game stats
   #     print("+++ game statistics +++")
  #      print(f"won: {percent_won:.2f} \t "
 #             f"lost: {percent_lost:.2f} \t ")

#
  #      print()
 #       print("thanks for playing ")
#
#    else:
 #       print()
    #    print(" ❌❌❌ GAME OVER ❌❌❌ ")
        #print("u quit")

