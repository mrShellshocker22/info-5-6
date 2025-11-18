import  requests

while True:
    try:
        x = input("what university do you wanna know about?: " ).lower()

        universities = {
            "eac" : {"name" : "Eastern Arizona College", "Majors" : "50", "Cost" : "7,750", "Location" : "Thatcher"},
            "byu i" : {"name" : "Brigham Young University - Idaho", "Majors" : "100", "Cost" : "18325", "Location" : "Idaho"},
            "tecmilenio" : {"name" : "Tecmilenio", "Majors" : "24", "Cost" : "14000", "Location" : "Chihuahua"},
            "tec de monterrey" : {"name" : "Tecnologico de Monterrey","Majors" : "45", "Cost" : "135000", "Location" : "Ciudad Juarez"},
            "uacj" : {"name" : "Universidad Autónoma de Ciudad Juárez", "Majors" : "55", "Cost"  : 11520, "Location" : "Ciudad Juarez"},
        }

        name = universities[x]["name"]

        response = requests.get("http://universities.hipolabs.com/search?name=" + name)

        website = response.json()[0]["web_pages"][0]

        universities[x].setdefault("Website", website)

        print(f"{x} : {universities[x]}")
        break
    except ValueError:
        print("sorry, something went worng please try it again ")
    except KeyError:
        print("sorry, something went worng please try it again ")
