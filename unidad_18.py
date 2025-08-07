"""Module providing a function printing python version."""

# /*
#  * UNIDAD 18: ITERACIONES
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  * /----------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Mecanismo para iteraciones 1

for i in range(1, 11):
    print(f"Imprimir for: {i}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Mecanismo para iteraciones 2

N = 1
while N <= 10:
    print(f"Imprimir while: {N}")
    N += 1
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Mecanismo para iteraciones 3


def imprimir_numero(numero):
    """Funcion recursiva que imprime numeros del 1 al 10"""
    if numero <= 10:
        print(f"Imprimir recursivo: {numero}")
        imprimir_numero(numero+1)


imprimir_numero(1)
# -----------------------------------------------------------------------------------
