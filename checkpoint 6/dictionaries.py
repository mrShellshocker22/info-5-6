capitals = {
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasília",
}

capitals["Italy"] = "Rome" #add a new key and value
del capitals["Brazil"] #delete a key
capitals.pop("Canada") 
capitals.clear() 

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for key in students:
#     print(f"{key}: {key}")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for element in students:
    print(f"{element["name"]} is in {element["house"]}, {element["patronus"]}")