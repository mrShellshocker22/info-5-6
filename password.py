import getpass
def main():
    password =getpass.getpass("Please enter your password: ") 
    confirm_password(password)


def confirm_password(password):
      tries_left = 3
      while True:
            
            check1 = input(f"Please confirm your password, you have {tries_left} tries left: ") 

            if check1 == password:
                guess_password(password)
                break
            if tries_left == 1:
                  print("You ran out of tries bye bye")
                  break
            if check1 != password:
                  print("Passwords did not match.")
                  tries_left -= 1

def guess_password(password):
    print("Hey try to guess the password")
    guess = input("Enter your guess: ")  
    if guess == password:
            print("Congrats! You guessed the password")
    else :
            print("Womp Womp you failed")

main()