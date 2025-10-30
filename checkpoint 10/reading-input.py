def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)

def read_input(prompt, small, large): # Insert missing parameters
  while True:
    try:
      x = int(input(prompt))
      if x > 5 and x < 10:
        return x
      else: 
        ("please type a NUMBER between", small, "and", large)
    except ValueError:
      print("please type a NUMBER between", small, "and", large)


main()