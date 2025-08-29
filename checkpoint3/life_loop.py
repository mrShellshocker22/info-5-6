import time
def main():
    print("Ey yo papito, how you doing?...")

    loop()

def loop():

    while True:
        response = input("Are you ready to play some SHELL SHOCKERsito 😝😝😝 (yes/no): ")

        if response == "yes":
            print("Letss GOOO!!!")
            print("https://shellshock.io/")
            break
        
        elif response == "no":
            print("aight... Ill wait for you")
            time.sleep(4)
            

        else:
            print("ye ye ye what ever... ")
            time.sleep(4)
        
main()