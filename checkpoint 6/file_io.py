# names = []

# for i in range(3):

#     name = input("What is your name: ")
#     print(f"gaboHello {name}")
#     names.append(name)

# name = input("Whats your name?: ")
#file = open("name.txt", "w")
# file.write(f"name\n")
# file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{input("whats your name?: ")}")

with open("name.txt", "r") as file:
    lines = sorted(file.readlines())

for line in lines:
    print(f"Hello {line.rstrip()}")