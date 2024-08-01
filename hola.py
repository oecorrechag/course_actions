import os

def main():
	nombre = os.getenv("USERNAME")
	print(f"¡Hola SEGUNDO, {nombre} desde Github!")

if __name__ == '__main__':
	main()
	