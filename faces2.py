
def main():

    face = input("make a face :) or :( \t")
    convert(face)
    
def convert(message):
    message = message.replace(":)", "😊".replace(":(","🙁"))
    convert(message)

main()