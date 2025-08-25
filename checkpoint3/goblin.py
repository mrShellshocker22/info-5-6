import random
print("Wellcome to the goblin game")
print("The best game ever")
player_name = input("What is your name? ")
print(f"{player_name}, can you find the goblin?")
print("|_|_|_|_|_|")
goblin_position = random.randint(1, 5)

keep_trying = True
while keep_trying:
    guess = int(input("Can you guess where the goblin is? "))

    if guess == goblin_position:
        print("You found the goblin!")
        keep_trying = False
    else:
        print("NO!! the goblin is still out there")