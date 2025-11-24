import requests

correct_names = {"simplify": "simplify", "factor": "factor", "derive": "derive", "integrate": "integrate", "zeroes": "zeroes", 
                 "tangent": "tangent", "area": "area", "cosine": "cos", "sine": "sin", "tangent": "tan", "inverse cosine": "arccos", 
                 "inverse sine": "arcsin", "inverse tangent": "arctan", "absolute value": "abs", "logarithm": "log"}

while True:
    type_operation = input("What type of operation you want to do?, we have \nSimplify, Factor, Derive, Integrate, Cosine, Sine, Tangent, etc.\n").lower()
    expression = input("Awesome, now enter the expression you want to solve\n")
    verbs = { "derive" : "derivative", "simplify" : "simplification", "factor" : "factorization", "integrate" : "integral" }

    try:
        answer = requests.get("https://newton.vercel.app/api/v2/"+ correct_names[type_operation] + "/" + expression)
        break
    except KeyError:
        print("This ain't an operation, please try again")

try:
    print(f"The {verbs[answer.json()["operation"]]} of {answer.json()["expression"]} is: {answer.json()["result"]}")
except KeyError:
    print(f"The {answer.json()["operation"]} of {answer.json()["expression"]} is: {answer.json()["result"]}")