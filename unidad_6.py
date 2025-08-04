"""Module providing a function printing python version."""

# /*
#  * UNIDAD 6:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como
#  * variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime
#  *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
#  *   su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  * /-----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Tipos inmutables (como int, float, str, bool, tuple) se comportan como "por valor".
# Tipos mutables (como list, dict, set, objetos) se comportan como "por referencia".
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# ASIGNACION POR VALOR

A = 10
B = A  # B recibe el valor de A, no una referencia a A
B += 5  # B ahora es 15, A sigue siendo 10
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# ASIGNACION POR REFERENCIA

LISTA_1 = [1, 2, 3]
LISTA_2 = LISTA_1  # LISTA_2 recibe una referencia a LISTA_1
LISTA_2.append(4)  # Modifica LISTA_2, pero también afecta a LISTA_1
# Ahora LISTA_1 es [1, 2, 3, 4] y LISTA_2 es [1, 2, 3, 4]
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# PASO DE VARIABLES POR VALOR Y POR REFERENCIA

# Función que recibe un entero (por valor)


def incrementar(numero):
    """Incrementa el valor de 'numero' en 1."""
    numero += 1  # Incrementa el valor local de 'numero'
    print(f"Valor dentro de la función: {numero}")


NUMERO = 5
incrementar(NUMERO)  # NUMERO sigue siendo 5 después de la llamada
print(f"Valor fuera de la función: {NUMERO}")  # Imprime 5

# Función que recibe una lista (por referencia)


def agregar_elemento(lista):
    """Agrega un elemento a la lista."""
    lista.append(4)
    print(f"Lista dentro de la función: {lista}")


LISTA = [1, 2, 3]
agregar_elemento(LISTA)  # LISTA ahora es [1, 2, 3, 4]
print(f"Lista fuera de la función: {LISTA}")  # Imprime [1, 2, 3, 4]

# Evitar la modificación de una lista original al pasarla por valor


def agregar_elemento_copia(lista):
    """Agrega un elemento a una copia de la lista."""
    lista_copia = lista.copy()
    lista_copia.append(5)
    print(f"Lista copia dentro de la función: {lista_copia}")


LISTA_ORIGINAL = [1, 2, 3]
agregar_elemento_copia(LISTA_ORIGINAL)  # LISTA_ORIGINAL sigue siendo [1, 2, 3]
# Imprime [1, 2, 3]
print(f"Lista original fuera de la función: {LISTA_ORIGINAL}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA


def por_valor(a, b):
    """Intercambia dos valores y los retorna."""
    temporal = a
    a = b
    b = temporal
    return a, b


NUMERO_A = 5
NUMERO_B = 10
NUMERO_C, NUMERO_D = por_valor(NUMERO_A, NUMERO_B)
print(f"Valores originales: A={NUMERO_A}, B={NUMERO_B}")
print(f"Valores intercambiados: C={NUMERO_C}, D={NUMERO_D}")


def por_referencia(lista_a, lista_b):
    """Intercambia dos listas y las retorna."""
    temporal = lista_a[:]
    lista_a[:] = lista_b[:]
    lista_b[:] = temporal
    return lista_a, lista_b


LISTA_A = [1, 2, 3]
LISTA_B = [4, 5, 6]
LISTA_C, LISTA_D = por_referencia(LISTA_A, LISTA_B)
print(f"Listas originales: A={LISTA_A}, B={LISTA_B}")
print(f"Listas intercambiadas: C={LISTA_C}, D={LISTA_D}")
# -----------------------------------------------------------------------------------
