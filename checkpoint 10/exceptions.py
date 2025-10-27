#Syntax error
#print("Hello, world")

# Value Error
# try:
#     x = int(input("Whats x?: "))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")


# def spam(divided_by):
#     try:
#         return 42 / divided_by
#     except ZeroDivisionError:
#         print("what ever you want")
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# while True:
#     try:
#         x = int(input("Whats x?: "))
    
#     except ValueError:
#         print("x is not a number") 
#     else: 
#         break
# print(f"x is equal to {x}")

def read_small_integer():
    while True:
        try:
            input_str = input("enter a small integer: ")
            number = int(input_str)
            if number < 100 and number >= 0: 
                return number
        except ValueError:
            pass 
        print("invalid input")
        
number = read_small_integer()
print(number, "to the power of 3 is ", number ** 3)