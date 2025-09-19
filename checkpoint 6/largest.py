def main():
    list_length = int(input("how many numbers do you want on your list?: "))
    
    loop(list_length)

def loop(list_lenght):
    list = []
    for i in range(list_lenght):

        
        numbers = int(input("enter a number to add to the list: "))

        list.append(numbers)
        
    print(f"{list}")

    with open("largest.txt", "w") as file:
        for line in list:
            file.write(f"{list}")


main()