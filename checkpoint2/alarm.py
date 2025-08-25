def main():
    is_armed = True
    motion_detected = False
    door_open = True
    is_afternoon = False
    display_alarm(is_armed, motion_detected, door_open, is_afternoon)

def display_alarm(iar, ms, dop, an):
    if iar:
        if ms:
            print("INTRUDER!!!")
        if dop:
            print("door is open")
    else:
        if an and ms:
            print("Welcome home, turn the light on")

main()