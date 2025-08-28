def main():

    step_size = int(input("enter the star: "))
    number = int(input("enter the limit:  " ))

    loop(number,step_size)

def loop(number,step_size):
    start = step_size
    while True:

        print(f"{step_size}", end=', ')

        step_size = step_size + start

        if step_size > number:
            break

main()