def main():

    name = input("Whats your name? ").strip().title() 
    hello(name) 

def hello(to="World"):
    print(f"Hello,{to}")
main()