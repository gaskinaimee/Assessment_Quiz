# The yes/no function. If user responds with "yes" the program continues. If they say "no", the program will
# display the instructions.
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response =="n":
            response = "no"
            return response
        else:
            print("Please answer with either yes or no.")

# The instructions function. This is the function that explains what the instructions are and when to show them.
def instructions():
    print("***** How to Play *****")
    print("")
    return instructions

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()
else:
    print("Continue program.")
