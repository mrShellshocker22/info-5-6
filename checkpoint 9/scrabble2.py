def random_13_letters(): # this funtion give us the 13 random letters we are gonna use to play
    import random # random 
    alphabet = ["A","A","A","A","A","A","A","A","A", #we are giving more vocals so they can make more words 
                "B","B",
                "C","C",
                "D","D","D","D",
                "E","E","E","E","E","E","E","E","E","E","E","E",
                "F","F",
                "G","G","G",
                "H","H",
                "I","I","I","I","I","I","I","I","I",
                "J",
                "K",
                "L","L","L","L",
                "M","M",
                "N","N","N","N","N","N",
                "O","O","O","O","O","O","O","O",
                "P","P",
                "Q",
                "R","R","R","R","R","R",
                "S","S","S","S",
                "T","T","T","T","T","T",
                "U","U","U","U",
                "V","V",
                "W","W",
                "X",
                "Y","Y",
                "Z"]
    letters_13 = [] # here we are gonna save the words that we are gonna use

    for i in range(0,13):   # here we are just "choosing" the 13 letters
        i = random.choice(alphabet) 
        letters_13.append(i)
    
    return " ".join(letters_13), letters_13 # we show them the letters

def score(word): # here we assign the points that each letter has
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    score = 0 # we set  our score to 0
    for i in word: # we check the letters in the word we are gonna write and then it adds the points to the score
        for point, letters in score_chart.items():
            if i in letters:
                score += point
    return score # prints the socre each time

while True: 
    letters, list_letters = random_13_letters()
    print(letters)
    word = input("type your word: ").upper()
    wrong_characters = []

    if word == "": # if you dont write anything it stops the game
        print("Game Over")
        print(f"Your final score is {score(word)}")
        break

    valid = True
    for i in word: 
        if i in list_letters:
            list_letters.remove(i) # if we already use the letter it takkes it out of the list
        else:
            wrong_characters.append(i)
            valid = False

    if not valid: # if theres latter that is not in the list it tells you 
        print(f"Invalid input you do not have: {wrong_characters}")
        continue

    with open("words.txt", "r") as file: # it checks the document where we have all the words 
        words = {word.lower() for word in file.read().splitlines()}

    if word.lower() not in words: # if the word we put is not in the document it tells you so 
        print("Not a valid word")
        continue

    if word.lower() in words: # if the word is in the document it tells you your score 
        print(f"your score is {score(word)}")