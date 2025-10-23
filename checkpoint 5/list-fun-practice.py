def main():
    values = [ ]
    setp_one(values)
    length(values)
    mean(values)
    
def setp_one(values):

    while True:

        elements = int(input("enter a number to add to the list (enter 0 to end program): "))

        if elements == 0:
            print("program is finished")
            print(f"input: {values}")
            values.sort()
            print(f"sorted: {values}")
            break

        values.append(elements)

        print(f"input: {values}")
        values.sort()
        print(f"sorted: {values}")


def length(values):
    the_length = len(values)
    print(f"The length of the list is: {the_length}")

def mean(values):
    the_mean = sum(values) / len(values)
    print(f"The mean of the list is: {the_mean}")

def range_of_list(values):
    the_range = max(values) - min(values)

main()