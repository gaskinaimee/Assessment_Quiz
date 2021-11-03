import random
score = 0
rounds = int(input("How many rounds would you like to play?"))

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
             "Who invented jeans?",
             "What do algophobics fear?",
             "Which creature in Greek mythology was half-man and half-bull?",
             "What chemical element has the atomic number 18?",
             "What is the fourth sign of the Zodiac?",
             "How many stripes are there on the US flag?"]

answer_list = [["portugese"], ["206", "two hundred and six"], ["france"], ["traissic", "triassic period",
            "the triassic period"], ["saturn"], ["norway"], ["the world wide web", "world wide web"],
            ["1604"], ["3", "three"], ["william shakespeare", "shakespeare"], ["caravan"],
           ["miss trunchbull"], ["rice"], ["the bible"], ["levi struass"], ["pain"], ["minotaur"],
           ["argon", "ar"], ["cancer"], ["thirteen", "13"]]

if rounds == 5:
    print("You have chosen to play 5 rounds!")
    rounds += 1
elif rounds == 10:
    print("You have chosen to play 10 rounds!")
elif rounds == 15:
    print("You have chosen to play 15 rounds!")
elif rounds == 20:
    print("You have chosen to play 20 rounds!")
else:
    print("Please enter either 5, 10, 15, or 20 rounds.")


  #Check if the user's answer is in the corresponding row
for question in question_list:
    print(question[0])
    answer = answer_list[0]
    if answer == answer_list[0]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
