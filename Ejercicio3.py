def evaluar_expresion(expresion):
    
    try:
        resultado = eval(expresion)
        return resultado
    except (SyntaxError, TypeError, NameError):
        print("Error: Expresión inválida.")
        return None

if __name__ == "__main__":
    expresion_entrada = input("Ingrese la expresión aritmética a evaluar: ")
    resultado = evaluar_expresion(expresion_entrada)

    if resultado is not None:
        print(f"El resultado de la expresión '{expresion_entrada}' es: {resultado}")