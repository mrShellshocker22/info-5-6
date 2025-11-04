
food_dic = {
    "Banana" : 33,
    "Oranges" : 21,
    "Carrots" : 13,
    "Lettuce" : 1,
    "Ham" : 123,
    "Tuna" : 45,
    "Beans" : 113,
    "Edamame" : 127,
    "Ranch" : 29,
    "Milk" : 73,
    "Watermelon" : 11
}

while True:
    try:

        combination = input("Write two elements (put a coma in between): ")
        combination_list = combination.split(",")

        element_1 = combination_list[0].strip()
        element_2 = combination_list[1].strip()

        if combination == "Milk,Watermelon" or combination == "Watermelon,Milk":
            print("sorry you can not combine Milk and Oranges\n")

        print(f"The combination of calories of {element_1} and {element_2} is: {food_dic[element_1] + food_dic[element_2]}")
    except KeyError:
        print("sorry we dont know the calories of this combination\n")
    except IndexError:
        print("please enter two elements separated by a comma, with no spaces\n")
    