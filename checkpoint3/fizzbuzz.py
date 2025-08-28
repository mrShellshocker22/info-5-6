number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")

elif number % number == 0 and number % 2 != 0 and number % 3 != 0:
    print("prime number")

else:
    print(number)