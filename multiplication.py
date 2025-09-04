def main():
    number = int(input("enter a positive number: "))
    if number > 0:
        multiplication(number)
    else:
        print("please follow the instructions")

def multiplication(number):

    i = 1


    while i <= 10:

            print(f"{number} X {i} = {number * i}")
            i += 1

main()