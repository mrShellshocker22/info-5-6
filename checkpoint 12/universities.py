
universities = {
    "Eastern Arizona College" : {"Majors" : , "Cost" : 7750, "Distance" : 428, "Location" : "Thatcher"},
    "BYU Pathway" : {"Majors" : , "Cost" : 18325, "Distance" : , "Location" : "Idaho" },
    "Tec Milenio" : {"Majors" : , "Cost" : 14000, "Distance" : , "Location : "Chihuahua" },
    "Tec Monterrey CDJ" : {"Majors" : , "Cost" : 135000, "Distance" : , "Location" : "Ciudad Juarez"},
    "UACJ" : {"Majors" : , "Cost"  : 11520, "Distance" : , "Location" : "Ciudad Juarez"},
    }

try:
    x = input("what university do you wanna know about?: " )
    print(universities)
except ValueError,IndexError:
    print("something went off, please try again")