def ask_question (question, answer):
    error = "enter a letter"
    valid = False
    while not valid:
        try:
            response = input(question)
            if response == answer:
                print("You are correct!")
                return response
            else:
                print("You are incorrect!")
                return response
        except ValueError:
            print(error)

question_1 = ask_question("What language is spoken in Brazil? \n(a) Portuguese \n(b) Bengali \n(c) Spanish", "a")
question_2 = ask_question("How many bones are there in the average adult human body? \n(a) 155 \n(b) 206 \n(c) 215", "b")
question_3 = ask_question("Which country is brie cheese originally from? \n(a) France \n(b) Denmark \n(c) Italy", "a")
question_4 = ask_question("Which came first, the Jurassic or Triassic Period? \n(a) Jurassic Period \n(b) Triassic Period", "b")
question_5 = ask_question("Which planet has the most moons? \n(a) Saturn \n(b) Jupiter \n(c) Venus", "a")
question_6 = ask_question("Which country awards the Nobel Peace Prize? \n(a) Scotland \n(b) England \n(c) Norway", "c")
question_7 = ask_question("What does “www” stand for? \n(a) wide world web \n(b) web world wide \n(c) world wide web", "c")
question_8 = ask_question("When was the first dictionary published? \n(a) 1776 \n(b) 1806 \n(c) 1604", "c")
question_9 = ask_question("How many hearts does an octopus have? \n(a) 3 \n(b) 4 \n(c) 5", "a")
question_10 = ask_question("Who invented the word 'vomit'? \n(a) William Shakespeare \n(b) Charles Dickens \n(c) Henry James", "a")
question_11 = ask_question("What is the collective name for a group of camels? \n(a) an armoury \n(b) a camp \n(c) a caravan", "c")
question_12 = ask_question("What is the name of the headteacher in Roald Dahl's Matilda? \n(a) Miss Honey \n(b) Miss Trunchbull", "b")
question_13 = ask_question("What is Japanese sake made from? \n(a) Grapes \n(b) Rice \n(c) Grains", "b")
question_14 = ask_question("What's the best selling book of all time? \n(a) The Bible \n(b) Harry Potter and the Half Blood Prince \n(c) The Lord of the Rings", "a")
question_15 = ask_question("Who invented jeans? \n(a) Madewell \n(b) Just Jeans \n(c) Levi Strauss", "c")
question_16 = ask_question("What do algophobics fear? \n(a) Being alone \n(b) Eyes \n(c) Pain", "c")
question_17 = ask_question("What chemical element has the atomic number 18? \n(a) Magnesium \n(b) Helium \n(c) Argon", "c")
question_18 = ask_question("What is the fourth sign of the Zodiac? \n(a) Cancer \n(b) Taurus \n(c) Aries", "a")
question_19 = ask_question("Which creature in Greek mythology was half-man and half-bull? \n(a) Sirens \n(b) Minotaur \n(c) Minotaur", "c")
question_20 = ask_question("How many stripes are there on the US flag? \n(a) 12 \n(b) 13 \n(c) 14", "b")
