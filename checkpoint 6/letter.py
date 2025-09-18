def main():
  names = ["Mario","Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]
  loop(names)
 
def loop(names):

  for guest in names:
    receiver = guest
    sender = names[5]
    if receiver == names[5]:
      print("")
    else:

      print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """)
main()
