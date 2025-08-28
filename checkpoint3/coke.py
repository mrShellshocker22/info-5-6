def main():
    name = input("Hello, Whats your name?: ")
    print(f"Awesome {name}, cokes are 50 cents you can insert coins of 25, 10 and 5 cents")
    coke_value = 50
    loop(name,coke_value)

def loop(name,coke_value):
    while True:
        print(f"you're missing {coke_value}")
        dinero = int(input("Please insert a coin: "))

        if dinero != 25 or dinero != 10 or dinero != 5:
            print("sorry we only accept cons of 25, 10 or 5 cents")
            loop(name,coke_value)
            
        coke_value = coke_value - dinero

        if coke_value <= 0:
            print(f"Here you go {name}")

        break
main()
