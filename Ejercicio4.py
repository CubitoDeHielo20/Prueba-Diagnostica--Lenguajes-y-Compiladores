def ConteoPalabras():
    print("Conteo de ocurrencias de una palabra en una cadena")
    print("----------------------------------------------------")

    lenguaje = input("Ingrese el nombre del lenguaje L: ")
    cadena = input(f"Ingrese la cadena C escrita en {lenguaje}: ")
    palabra_buscar = input("Ingrese la palabra E a buscar: ")

    ocurrencias = cadena.count(palabra_buscar)

    print(f"\nCadena ingresada (en {lenguaje}):")
    print(cadena)
    print(f"\nLa palabra '{palabra_buscar}' aparece {ocurrencias} veces en la cadena.")

if __name__ == "__main__":
    ConteoPalabras()