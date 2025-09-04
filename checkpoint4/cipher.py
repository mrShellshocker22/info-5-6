def main(): # define la funcion principal
    message = input("Print a message to cipher: ").lower() #pedimos el input y mensaje que vamos a desifrar y el .lower es para que ls letras sean en minuscula como la tenemos en alphabet y cipher
    encode_message(message) # despues de pedir el mensaje ejecutamos la siguente funcion


def encode_message(text): #definimos la funcion que va a decifrar el mensaje

    alphabet = "abcdefghijklmnopqrstuvwxyz" #este va a ser un tipo de lista de todas las letras del alphabeto normal
    cipher = "zyxwvutsrqponmlkjihgfedcba" # este es la lista del alphabeto alreves
    new_message = "" #esta es una vriable indefinida entonces aqui vamos a ir poniendo las letras del mensaje codificado
    i = 0 # es el contador del index


    while i < len(text): # es el loop que va a buscar cada letra en el alphabeto y encontrar la letra del cipher que corresponde

        char = text[i] #esto significa que ahora char es la letra del mensaje que este asignada el index
        if char in alphabet: #si la letra char esta dentro de la lista alphabet entonces
            cipher_index = alphabet.find(char) #creamos otra variable que va a ser el numbero especifico de la letra en el alphabet, alphabet.find(char) es para identificar ese numero
            new_message += cipher[cipher_index] #ahora le vamos a agregar o "concatenar" la letra del cipher que corresponde a la del alphabet
        else:new_message += char #si la letra o el caracter no esta en el alphabet entonces lo pone ahi igual como espacios o numeros
        i += 1 #ya que cifraste la letra en la que estas trabajando, avanza a la siguente letra
    print(new_message) #ya que termina el loop imprime el texto 

main()