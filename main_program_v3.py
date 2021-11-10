import random
rounds = 1
score = 0

question_list = ["What language is spoken in Brazil?",
                 "How many bones are there in the average adult human body?",
                 "Which country is brie cheese originally from?",
                 "Which came first, the Jurassic or Triassic Period?",
                 "Which planet has the most moons?",
                 "Which country awards the Nobel Peace Prize?",
                 "What does “www” stand for in a website browser?",
                 "When was the first dictionary published?",
                 "How many hearts does an octopus have?",
                 "Who invented the word 'vomit'?",
                 "What is the collective name for a group of camels?",
                 "What is the name of the headteacher in Roald Dahl's Matilda?",
                 "What is Japanese sake made from?",
                 "What's the best selling book of all time?",
                 "Who invented jeans?", "What do algophobics fear?",
                 "Which creature in Greek mythology was half-man and half-bull?",
                 "What chemical element has the atomic number 18?",
                 "What is the fourth sign of the Zodiac?",
                 "How many stripes are there on the US flag?"
                 "What's the biggest animal in the world?"]

answer_list = ["portuguese",
               "206",
               "france",
               "triassic period",
               "saturn",
               "norway",
               "world wide web",
               "1604",
               "3",
               "william shakespeare",
               "caravan",
               "miss trunchbull",
               "rice",
               "the bible",
               "levi strauss",
               "pain",
               "minotaur",
               "argon",
               "cancer",
               "13",
               "blue whale"]

def instructions():
    print("***** How to Play *****")
    print("First, you'll be asked how many rounds you want to play. \n"
          "You can choose to play 5 rounds, 10 rounds, 15 rounds or 20 rounds. \n"
          "The game will then begin. You will be asked a question and 3 possible answers will be displayed.\n "
          "Choose the answer you think is correct and type in the first letter of the answer. For example... \n"
          "What is the best colour? \na.) Red \nb.) Blue \nc.) Green \n"
          "You will have to type in either a, b or c.")
    return instructions

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

def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


while yes_no == "n":
    print(instructions)



statement_generator("Welcome to the General Knowledge quiz!", "*")
print()
played_before = yes_no("Have you played the game before? ")

# Main routine...
print("***** ROUND {} *****".format(rounds))
question1 = input(question_list[0]).lower()
if question1 == "portugese":
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[0]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question2 = input(question_list[1]).lower()
if question2 == answer_list[1]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[1]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question3 = input(question_list[2]).lower()
if question3 == answer_list[2]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[2]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question4 = input(question_list[3]).lower()
if question4 == answer_list[3]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[3]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question5 = input(question_list[4]).lower()
if question5 == answer_list[4]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[4]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question6 = input(question_list[5]).lower()
if question6 == answer_list[5]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[5]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question7 = input(question_list[6]).lower()
if question7 == answer_list[6]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[6]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question8 = input(question_list[7]).lower()
if question8 == answer_list[7]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[7]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question9 = input(question_list[8]).lower()
if question9 == answer_list[8]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[8]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question10 = input(question_list[9]).lower()
if question10 == answer_list[9]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[9]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question11 = input(question_list[10]).lower()
if question11 == answer_list[10]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[10]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question12 = input(question_list[11]).lower()
if question12 == answer_list[11]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[11]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question13 = input(question_list[12]).lower()
if question13 == answer_list[12]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[12]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question14 = input(question_list[13]).lower()
if question14 == answer_list[13]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[13]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question15 = input(question_list[14]).lower()
if question15 == answer_list[14]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[14]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question16 = input(question_list[15]).lower()
if question16 == answer_list[15]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[15]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question17 = input(question_list[16]).lower()
if question17 == answer_list[16]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[16]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question18 = input(question_list[17]).lower()
if question18 == answer_list[17]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[17]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question19 = input(question_list[18]).lower()
if question19 == answer_list[18]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[18]))
rounds += 1

print("***** ROUND {} *****".format(rounds))
question20 = input(question_list[19]).lower()
if question20 == answer_list[19]:
    score += 1
    print("Correct! Your score is {}.".format(score))
else:
    print("Wrong! The correct answer is {}.".format(answer_list[19]))

print("~~~ YOUR TOTAL SCORE IS {} ~~~".format(score))

if score <= 5:
    print("Nice try!")
elif score <= 10:
    print("Nice try! You still have a little bit to work on!")
elif score > 10:
    print("Nice work! You got more than half right! I think next time you can get a higher score!")
else:
    print("Woah, you did great! Awesome!")

statement_generator("Thank you for playing the General Knowledge Quiz!",  "*")
