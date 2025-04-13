def generar_coeficientes(n):
   
    if n < 0:
        return []
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        fila_anterior = [1, 1]
        for _ in range(2, n + 1):
            fila_actual = [1]
            for j in range(len(fila_anterior) - 1):
                fila_actual.append(fila_anterior[j] + fila_anterior[j + 1])
            fila_actual.append(1)
            fila_anterior = fila_actual
        return fila_actual

def mostrar_polinomio(coeficientes):
   
    grado = len(coeficientes) - 1
    terminos = []
    for i, coeficiente in enumerate(coeficientes):
        if coeficiente != 0:
            if grado - i == 0:
                terminos.append(str(coeficiente))
            elif grado - i == 1:
                terminos.append(f"{coeficiente}x")
            else:
                terminos.append(f"{coeficiente}x^{grado - i}")
    return " + ".join(terminos) if terminos else "0"

def evaluar_polinomio_simple(coeficientes, x):
    
    grado = len(coeficientes) - 1
    resultado = 0
    print(f"\nEvaluando f({x}) = (x+1)^{grado}:")
    for i, coeficiente in enumerate(coeficientes):
        potencia = grado - i
        termino = coeficiente * (x ** potencia)
        print(f"  Término {i+1}: {coeficiente} * ({x}^{potencia}) = {termino}")
        resultado += termino
    print(f"f({x}) = {resultado}")

if __name__ == "__main__":
    try:
        n = int(input("Ingrese un número entero no negativo n: "))
        if n < 0:
            print("Por favor, ingrese un número entero no negativo.")
        else:
            # a) Generar y mostrar los coeficientes del polinomio
            coeficientes = generar_coeficientes(n)
            print(f"\nLos coeficientes de (x+1)^{n} son: {coeficientes}")

            # Mostrar el polinomio
            polinomio_str = mostrar_polinomio(coeficientes)
            print(f"El polinomio (x+1)^{n} es: {polinomio_str}")

            # b) Evaluar el polinomio para un x dado
            try:
                valor_x = float(input("Ingrese el valor de x para evaluar el polinomio: "))
                evaluar_polinomio_simple(coeficientes, valor_x)
            except ValueError:
                print("Por favor, ingrese un valor numérico para x.")

    except ValueError:
        print("Por favor, ingrese un número entero válido para n.")