def main():

    setp_one()


def setp_one():
    list = [ ]
    while elements > 0:
        
        elements = int(input("enter a number to add to the list"))
        list.append(elements)

        print(list)
        list.sort()
        print(list)

main()