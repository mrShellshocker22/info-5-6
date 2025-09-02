def main():
    message = input("Print a message to cipher: ").lower()
    encode_message(message)


def encode_message(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0


    while i > len(text):
        if text[0] == alphabet[i]:
            print(cipher[i])
        else:
            i += 1
            char = text