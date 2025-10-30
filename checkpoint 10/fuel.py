
while True:
    try:
        x = input("enter a fraction (like 1/2): ").split("/") 
        
        num = int(x[0])
        den = int(x[1])
        percentage = round((num / den) * 100)


        if percentage <= 1:
            print("Your tank is: E")
            break
        if percentage >=  99 and percentage <= 100:
            print("Your tank is: F")
            break
        else:
            print(percentage)
            break
    except ZeroDivisionError:
        print("Input invalid, please try again")
        pass
    except ValueError:
        print("Input invalid, please try again")
        pass
    except IndexError:
        print("Input invalid, please try again")
        pass
