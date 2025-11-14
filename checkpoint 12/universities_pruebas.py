import  requests

x = input("what university do you wanna know about?: " )
response = requests.get("http://universities.hipolabs.com/search?name=" + x)


website = response.json()[0]["web_pages"][0]

universities = {
    "EAC" : {"name" : "Eastern Arizona College", "Majors" : "50", "Cost" : "7750", "Location" : "Thatcher", "Website" : website}
}

print(universities)