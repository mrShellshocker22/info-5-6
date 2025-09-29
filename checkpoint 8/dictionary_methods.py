dictionary = {
    "color": "black",
    "age" : 29,
}
#values
print(dictionary.values())
for v in dictionary.values():
    print(v)
#keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)
#items
print(dictionary.items())
for i in dictionary.items():
    print(i)

for k,v in dictionary.items():
    print(f"{k} -> {v}")

#get

print_items = {"apples": 5, "cups": 2}
print(f"I'm bringing {print_items.get('cups')} cups")
print(f"I'm bringing {print_items.get('eggs', 0)} eggs")

#setting default values
pet_info = {
    "name": "Puka",
    "age": 5
 }

pet_info.setdefault("color", "black")
