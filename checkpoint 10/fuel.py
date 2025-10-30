
x = input("enter a fraction (like 1/2): ").split("/") 

num = int(x[0])
den = int(x[1])
percentage = round((num / den) * 100)

try:
    if percentage <= 1:
        print("Your tank is: E")
    if percentage >=  99 and percentage <= 100:
        print("Your tank is: F")
except ZeroDivisionError:
    print("Input invalid, please try again")
    

print(percentage)