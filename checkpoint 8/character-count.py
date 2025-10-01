def character_counter(message, dictionary): 
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
    print(dictionary)



message = input("Enter a message: ")

dictionary = {}
character_counter(message, dictionary)

print(f"your message have: {len(message)} characters")


