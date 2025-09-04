def main():
    number = int(input("enter a positive number: "))
    if number > 0:
        multiplication(number)
        tablas()
    else:
        print("please follow the instructions")

def multiplication(number):

    i = 1


    while i <= 10:

            print(f"{number} x {i} = {number * i}")
            i += 1

def tablas():
     
    e = 1
    a = 1
     
    print("hey do you know that")
    
    while e <= 10:
     print(f"{e} x {a} = {e * a}")
     
     a += 1
     if a > 10:
        e += 1
        a = 1
        print("")


main()