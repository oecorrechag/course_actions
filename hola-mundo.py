import os

def main():
    nombre = os.getenv("USERNAME")
    lenguaje_favorito = os.getenv("LANGUAGE")
    print(f"¡Hola, {nombre}, {lenguaje_favorito} desde GitHub!")

if __name__ == "__main__":
    main()
    