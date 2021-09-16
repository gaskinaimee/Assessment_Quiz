# Ask the user if they have played before.
show_instructions = input("Have you played this game before?").lower()
while show_instructions.lower() != "xxx":

# If the user responds with yes,
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program continues.")

    elif show_instructions == "no" or "n":
        show_instructions == "no"
        print("Display instructions.")
    else:
        print("Please answer with either yes or no.")
