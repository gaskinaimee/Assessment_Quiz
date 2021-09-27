rounds = int(input("How many rounds would you like to play?"))

if rounds == 5:
    print("You have chosen to play 5 rounds!")
elif rounds == 10:
    print("You have chosen to play 10 rounds!")
elif rounds == 15:
    print("You have chosen to play 15 rounds!")
elif rounds == 20:
    print("You have chosen to play 20 rounds!")
else:
    print("Please enter either 5, 10, 15, or 20 rounds.")

play_again = input("Press <Enter> to play...").lower()


while play_again == "":

    # Increase number of rounds played.
    rounds += 1


    # Print round number
    print("*** Round #{} ***".format(rounds))
