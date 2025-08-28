def main():
    name = input("Hello, Whats your name?: ")
    print(f"Awesome {name}, cokes are 50 cents you can insert coins of 25, 10 and 5 cents")
    coke_value = 50
    total_paid = 0
    loop(name,coke_value,total_paid)



def loop(name,coke_value,total_paid):
    while coke_value > 0:

        print(f"you're missing {coke_value}")
        pay = int(input("Please insert a coin: "))

        if pay == 25 or pay == 10 or pay == 5:
            coke_value = coke_value - pay
            total_paid = total_paid + pay
        else:
            print("not coin")

        if total_paid >= 50:
            print(f"Here you go {name}, aqui esta to coca")
            print(f"heres your change {total_paid - 50}")


main()
