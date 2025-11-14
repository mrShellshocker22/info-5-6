import requests
universities = {
    "Eastern Arizona College" : {"Majors" : "50", "Cost" : "7750", "Location" : "Thatcher", "Website" : ""},
    "Brigham Young University - Idaho" : {"Majors" : "30 online certificates", "Cost" : "18325", "Location" : "Idaho", "Website" : "" },
    "Tecmilenio" : {"Majors" : "24", "Cost" : "14000", "Location : "Chihuahua", "Website" : "" },
    "Tec Monterrey CDJ" : {"Majors" : "15", "Cost" : "135000", "Location" : "Ciudad Juarez", "Website" : "" },
    "UACJ" : {"Majors" : "55", "Cost"  : 11520, "Location" : "Ciudad Juarez", "Website" : "" },
    }

try:
    x = input("what university do you wanna know about?: " )
    response = requests.get("http://universities.hipolabs.com/search?name=" + x)
    print(response.json()[0]["web_pages"][0])

except ValueError,IndexError:

    print("something went off, please try again")