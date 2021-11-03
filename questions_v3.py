question_list = [["What language is spoken in Brazil?", "portugese"]
             ["How many bones are there in the average adult human body?", "206"]
             ["Which country is brie cheese originally from?", "france"]
             ["Which came first, the Jurassic or Triassic Period?", "triassic period"]
             ["Which planet has the most moons?", "saturn"]
             ["Which country awards the Nobel Peace Prize?", "norway"]
             ["What does “www” stand for in a website browser?", "world wide web"]
             ["When was the first dictionary published?", "1604"]
             ["How many hearts does an octopus have?", "3"]
             ["Who invented the word 'vomit'?", "william shakespeare"]
             ["What is the collective name for a group of camels?", "caravan"]
             ["What is the name of the headteacher in Roald Dahl's Matilda?", "miss trunchbull"]
             ["What is Japanese sake made from?", "rice"]
             ["What's the best selling book of all time?", "the bible"]
             ["Who invented jeans?", "levi struass"]
             ["What do algophobics fear?", "pain"]
             ["Which creature in Greek mythology was half-man and half-bull?", "minotaur"]
             ["What chemical element has the atomic number 18?", "argon"]
             ["What is the fourth sign of the Zodiac?", "cancer"]
             ["How many stripes are there on the US flag?", "13"]]

for question in question_list:
    print(question[0])
    answer = input("Answer: ")
    if answer == question[1]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is {}.".format(question[1]))
