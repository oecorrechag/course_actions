import os

def main():
    lenguaje_favorito = os.getenv("lenguaje_favorito")
    print(f"¡Hola, {lenguaje_favorito} desde GitHub!")

if __name__ == "__main__":
    main()
    