birthdays = {
    "gabo": "2008-07-28",
    "joseph": "2008-02-14",
    "hyrum": "2008-02-14" 
}

name = input("Enter a name: ")


if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
else:
    print(f"I do not have birthday information for {name}")
    date = input("What is their birthday?: ")
    birthdays[name] = (date)
    print(f"{birthdays[name]} is the birthday of {name}")
