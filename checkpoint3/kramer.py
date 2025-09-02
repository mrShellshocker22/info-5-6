while True:
    greeting = input("enter a greeting: ")

    if greeting == "hello":
        print("$0.00")
        break
    elif greeting.startswith("h"):
        print("you recive $20.00")
        break
    else:
        print("you recive $100.00")
        break