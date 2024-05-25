# Herramientas-finalhh
## Primero
usé el git clone para clonar el repositorio y despues el cd Herramientas-finalhh, despues creé la rama con el git branch "nicolas-guerrero" (nombre de la rama), conecté el mainh.py al repositorio con el codigo del primer punto y con el .gitignore realicé el 2

## Descripción
Este proyecto permite convertir caracteres y palabras a su representación en byte y viceversa, utilizando un menú interactivo.

##Codigo
def char_to_byte(character):
    """Genera la representación en byte de un carácter."""
    return format(ord(character), '08b')

def word_to_bytes(word):
    """Genera la representación en byte de una palabra."""
    return ' '.join(format(ord(char), '08b') for char in word)

def byte_to_ascii(byte_str):
    """Genera la representación ASCII de un byte."""
    ascii_char = chr(int(byte_str, 2))
    return f"{ascii_char}-{ord(ascii_char)}"

def menu():
    """Menú de opciones para el usuario."""
    while True:
        print("\nMenu:")
        print("1. Generar representación en byte de un carácter")
        print("2. Generar representación en byte de una palabra")
        print("3. Generar representación ASCII de un byte")
        print("4. Salir")

        choice = input("Elija una opción: ")

        if choice == '1':
            char = input("Ingrese un carácter: ")
            if len(char) == 1:
                print(f"Representación en byte: {char_to_byte(char)}")
            else:
                print("Por favor ingrese solo un carácter.")
        elif choice == '2':
            word = input("Ingrese una palabra: ")
            print(f"Representación en byte: {word_to_bytes(word)}")
        elif choice == '3':
            byte_str = input("Ingrese un byte (8 bits): ")
            if len(byte_str) == 8 and all(bit in '01' for bit in byte_str):
                print(f"Representación ASCII: {byte_to_ascii(byte_str)}")
            else:
                print("Por favor ingrese una cadena de 8 bits válida.")
        elif choice == '4':
            break
        else:
            print("Opción no válida, intente de nuevo.")
            
if __name__ == "__main__":
    menu()


## Menú de Opciones
1. Generar representación en byte de un carácter.
2. Generar representación en byte de una palabra.
3. Generar representación ASCII de un byte.
4. Salir.

## Uso
Clona el repositorio y ejecuta el archivo principal para interactuar con el menú:


## Funciones
- `char_to_byte(character)`: Toma un carácter y devuelve su representación en byte.
- `word_to_bytes(word)`: Toma una palabra y devuelve su representación en byte.
- `byte_to_ascii(byte_str)`: Toma un byte en forma de cadena de 8 bits y devuelve su carácter ASCII correspondiente.

## Comandos de Git Utilizados
- `git init`: Inicializar el repositorio.
- `git add .`: Añadir archivos.
- `git commit -m "Mensaje del commit"`: Confirmar cambios en el repositorio.
- `git branch nombre_de_la_rama`: Crear una nueva rama.
- `git checkout nombre_de_la_rama`: Cambiar a una rama diferente.
- `git merge nombre_de_la_rama`: Fusionar cambios de una rama a otra.
- `git push origin nombre_de_la_rama`: Subir cambios al repositorio remoto.

## Estructura del Proyecto
- `main.py`: Contiene el menú interactivo y la lógica principal del programa.
- `.gitignore`: Lista de archivos y directorios a excluir del repositorio.
- `README.md`: Documentación del proyecto.

## Información del Desarrollador
- Nombre: Nicolás Guerrero Maya
- GitHub: NicolasGM7
