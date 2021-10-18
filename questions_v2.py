import random
score = 0

questions = ["What language is spoken in Brazil?",
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

answers = [["Portugese", "Port"], ["206", "two hundred and six"], ["France"], ["traissic", "triassic period",
            "the triassic period"], ["saturn", "sat"], ["norway"], ["the world wide web", "world wide web"],
            ["1604", "sixteen hundreds"], ["3", "three"], ["william shakespeare", "shakespeare"], ["a caravan", "caravan"],
           ["Miss Trunchbull"], ["rice"], ["the bible", "bible"], ["Levi Struass", "Struass"], ["pain"], ["Minotaur"],
           ["Argon", "ar"], ["Cancer"], ["thirteen", "13"]]


random.shuffle(questions)
for question, answer_list in zip(questions, answers):
    guess = input(question).strip().lower()

  #Check if the user's answer is in the corresponding row
    if guess in answer_list:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was {}!".format(answer_list[0]))

