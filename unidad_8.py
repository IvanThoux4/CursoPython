"""Module providing a function printing python version."""

# /*
#  * UNIDAD 8:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la
#  *   sucesión de Fibonacci (la función recibe la posición).
#  * /-------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONCEPTO DE RECURSIVIDAD
# Es una técnica de programación donde una función se llama a sí misma para resolver
# un problema.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Función recursiva para imprimir números del 100 al 0


def imprimir_numeros(n):
    """Imprime números del 100 al 0 de forma recursiva."""
    if n < 0:
        return
    print(n)
    imprimir_numeros(n-1)


# Llamada a la función para iniciar la impresión
imprimir_numeros(100)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion recursiva para calcular el factorial de un número


def factorial(n):
    """Calcula e imprime el factorial de un numero de forma recursiva"""
    if n < 0:
        print("Los numeros negativos no son validos.")
        return
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Llamada a la función
print(f"El resultado del factorial es: {factorial(5)}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci


def fibonacci(n: int) -> int:
    """Calcula el valor de un elemento en la sucesión de Fibonacci de forma recursiva."""
    if n <= 0:
        print("Los numeros negativos o el cero no son posibles de calcular.")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


numero = int(input("Ingrese una posicion para determinar su valor: "))
print(f"El valor de la posicion '{numero}' es: {fibonacci(numero)}")
# -----------------------------------------------------------------------------------
