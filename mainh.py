def char_to_byte(character):
    return format(ord(character), '08b')

def word_to_bytes(word):
    return ' '.join(format(ord(char), '08b') for char in word)

def byte_to_ascii(byte_str):
    ascii_char = chr(int(byte_str, 2))
    return f"{ascii_char}-{ord(ascii_char)}"

def menu():
    while True:
        print("\nMenu:")
        print("1. Generar representacion en byte de un caracter")
        print("2. Generar representacion en byte de una palabra")
        print("3. Generar representacion ASCII de un byte")
        print("4. Salir")

        choice = input("Elija una opcion: ")

        if choice == '1':
            char = input("Ingrese un caracter: ")
            if len(char) == 1:
                print(f"Representacion en byte: {char_to_byte(char)}")
            else:
                print("Por favor ingrese solo un caracter.")
        elif choice == '2':
            word = input("Ingrese una palabra: ")
            print(f"Representacion en byte: {word_to_bytes(word)}")
        elif choice == '3':
            byte_str = input("Ingrese un byte (8 bits): ")
            if len(byte_str) == 8 and all(bit in '01' for bit in byte_str):
                print(f"Representacion ASCII: {byte_to_ascii(byte_str)}")
            else:
                print("Por favor ingrese una cadena de 8 bits valida.")
        elif choice == '4':
            break
        else:
            print("Opcion no valida, intente de nuevo.")
            
if __name__ == "__main__":
    menu()
