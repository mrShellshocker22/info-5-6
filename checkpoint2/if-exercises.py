def main():
    problem = input("Write a arithmetic expression ")
    calculator(problem)

def calculator(problem):
    print(f"The result of {problem} is: ")
    print(f"{float(eval(problem))}")
main()