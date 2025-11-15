import  requests

def main():

    universities = {
        "EAC" : {"name" : "Eastern Arizona College", "Majors" : "50", "Cost" : "7,750", "Location" : "Thatcher", "Website" : website},
        "Brigham Young University - Idaho" : {"name" : "Brigham Young University - Idaho", "Majors" : "100", "Cost" : "18325", "Location" : "Idaho", "Website" : website},
        "Tecmilenio" : {"name" : "Tecmilenio", "Majors" : "24", "Cost" : "14000", "Location" : "Chihuahua", "Website" : website },
        "Tec de Monterrey" : {"name" : "Tecnologico de Monterrey","Majors" : "45", "Cost" : "135000", "Location" : "Ciudad Juarez", "Website" : website },
        "UACJ" : {"name" : "Universidad Autónoma de Ciudad Juárez", "Majors" : "55", "Cost"  : 11520, "Location" : "Ciudad Juarez", "Website" : website },

    }

    my_function(universities)

def my_function(universities):
    x = input("what university do you wanna know about?: " )
    name = universities[x[0]]

    response = requests.get("http://universities.hipolabs.com/search?name=" + name)

    website = response.json()[0]["web_pages"][0]


    print(f"{x} : {universities[x]}")

main