import  requests

x = input("what university do you wanna know about?: " )
response = requests.get("http://universities.hipolabs.com/search?name=" + x)


website = response.json()[0]["web_pages"][0]

universities = {
    "Eastern Arizona College" : {"Majors" : "50", "Cost" : "7,750", "Location" : "Thatcher", "Website" : website},
    "Brigham Young University - Idaho" : {"Majors" : "100", "Cost" : "18325", "Location" : "Idaho", "Website" : website},
    "Tecmilenio" : {"Majors" : "24", "Cost" : "14000", "Location" : "Chihuahua", "Website" : website },
    "Tecnologico de Monterrey" : {"Majors" : "15", "Cost" : "135000", "Location" : "Ciudad Juarez", "Website" : website },
    "Universidad Autónoma de Ciudad Juárez" : {"Majors" : "55", "Cost"  : 11520, "Location" : "Ciudad Juarez", "Website" : website },

}

print(f"{x} : {universities[x]}")
