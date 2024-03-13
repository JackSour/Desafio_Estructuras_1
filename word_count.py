
import sys

try:
    with open(sys.argv[1], "r") as archivo:
        texto = archivo.read()
        palabras = len(set(texto.split()))
        letras = len(set(texto))
        print(f"El número de caracteres distintos es: {letras}")
        print(f"El número de palabras distintas es: {palabras}")
except IndexError:
    print("Por favor, ingrese el nombre del archivo como argumento.")


