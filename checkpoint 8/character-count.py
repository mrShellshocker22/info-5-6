def character_counter(message, dictionary): 
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1
    print(dictionary)



message = input("Enter a message: ")

dictionary = {}
character_counter(message, dictionary)

print(f"your message have: {len(message)} characters")

#alternative 1

values_list = list(dictionary.values())
keys_list = list(dictionary.keys())
largest = max(values_list)
print(f"the most repeated character is: {keys_list[largest]}, repeated {dictionary[keys_list[largest]]} times")


#alternative 2

largest_number2 = max(dictionary, key=dictionary.get)
print(f"the most repeated character is: {largest_number2}, repeated {dictionary[largest_number2]} times")


