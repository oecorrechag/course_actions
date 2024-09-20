import os

def main():
    lenguaje_favorito = os.getenv("LANGUAGE")
    print(f"¡Hola su lenguaje es: {lenguaje_favorito} desde GitHub!")

if __name__ == "__main__":
    main()
    