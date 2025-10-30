def  main():
    print("Factorial Calculator")
    x = int(input("Type a positive integer: "))
    print(f"{x}! = {calculator(x)}")


def calculator(n):

    if n <= 0:
        raise ValueError(f"The input was negative or zero")
    else:
        new_n = 1
        for i in range(2,n + 1):
            new_n = new_n * i
        return new_n

main()