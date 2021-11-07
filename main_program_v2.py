import random
points = 0
rounds = 1
question_wrong = 0

# The yes/no function. If user responds with "yes" the program continues. If they say "no", the program will
# display the instructions.
def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

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
def score():
    for answer in question:
        points = points + 1
        print(points)

# The instructions function. This is the function that explains what the instructions are and when to show them.
def instructions():
    print("***** How to Play *****")
    print("First, you'll be asked how many rounds you want to play. \n"
          "You can choose to play 5 rounds, 10 rounds, 15 rounds or 20 rounds. \n"
          "The game will then begin. You will be asked a question and 3 possible answers will be displayed.\n "
          "Choose the answer you think is correct and type in the first letter of the answer. For example... \n"
          "What is the best colour? \na.) Red \nb.) Blue \nc.) Green \n"
          "You will have to type in either a, b or c.")
    return instructions

statement_generator("Welcome to the General Knowledge quiz!", "*")
print()
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

def ask_question (question, answer):
    error = "enter a letter"
    valid = False
    while not valid:
        try:
            response = input(question)
            if response == answer:
                print("You are correct! Your score is {}.".format(score))
                return response
            else:
                print("You are incorrect!")
                return response
        except ValueError:
            print(error)

#Main Routine goes here...
print("!!!!! ROUND {} !!!!!".format(rounds))
question_1 = ask_question("What language is spoken in Brazil? \n(a) Portuguese \n(b) Bengali \n(c) Spanish", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_2 = ask_question("How many bones are there in the average adult human body? \n(a) 155 \n(b) 206 \n(c) 215", "b")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_3 = ask_question("Which country is brie cheese originally from? \n(a) France \n(b) Denmark \n(c) Italy", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_4 = ask_question("Which came first, the Jurassic or Triassic Period? \n(a) Jurassic Period \n(b) Triassic Period", "b")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_5 = ask_question("Which planet has the most moons? \n(a) Saturn \n(b) Jupiter \n(c) Venus", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_6 = ask_question("Which country awards the Nobel Peace Prize? \n(a) Scotland \n(b) England \n(c) Norway", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_7 = ask_question("What does “www” stand for? \n(a) wide world web \n(b) web world wide \n(c) world wide web", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_8 = ask_question("When was the first dictionary published? \n(a) 1776 \n(b) 1806 \n(c) 1604", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_9 = ask_question("How many hearts does an octopus have? \n(a) 3 \n(b) 4 \n(c) 5", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_10 = ask_question("Who invented the word 'vomit'? \n(a) William Shakespeare \n(b) Charles Dickens \n(c) Henry James", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_11 = ask_question("What is the collective name for a group of camels? \n(a) an armoury \n(b) a camp \n(c) a caravan", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_12 = ask_question("What is the name of the headteacher in Roald Dahl's Matilda? \n(a) Miss Honey \n(b) Miss Trunchbull", "b")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_13 = ask_question("What is Japanese sake made from? \n(a) Grapes \n(b) Rice \n(c) Grains", "b")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_14 = ask_question("What's the best selling book of all time? \n(a) The Bible \n(b) Harry Potter and the Half Blood Prince \n(c) The Lord of the Rings", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_15 = ask_question("Who invented jeans? \n(a) Madewell \n(b) Just Jeans \n(c) Levi Strauss", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_16 = ask_question("What do algophobics fear? \n(a) Being alone \n(b) Eyes \n(c) Pain", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_17 = ask_question("What chemical element has the atomic number 18? \n(a) Magnesium \n(b) Helium \n(c) Argon", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_18 = ask_question("What is the fourth sign of the Zodiac? \n(a) Cancer \n(b) Taurus \n(c) Aries", "a")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_19 = ask_question("Which creature in Greek mythology was half-man and half-bull? \n(a) Sirens \n(b) Minotaur \n(c) Minotaur", "c")
rounds += 1
print("!!!!! ROUND {} !!!!!".format(rounds))
question_20 = ask_question("How many stripes are there on the US flag? \n(a) 12 \n(b) 13 \n(c) 14", "b")

if score <= 5:
    print("You got a lot wrong. You have a bit to work on!")
elif score <= 10:
    print("Nice try! You still have a little bit to work on!")
elif score > 10:
    print("Nice work! You got more than half right! I think next time you can get a higher score!")
else:
    print("Woah, you did great! Awesome!")
print("Thank you for playing the General Knowledge Quiz! Your total score is {}.".format(score))
