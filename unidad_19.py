"""Module providing a function printing python version."""

# /*
#  * UNIDAD 19: CONJUNTOS
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
#  * /---------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONJUNTOS

# Conjunto inicial
conjunto = [1, 2, 3, 4, 5]
print(f"El conjunto inicial es: {conjunto}")

# Añadir un elemento al final
conjunto.append(6)
print(f"El conjunto despues de añadir al final es: {conjunto}")

# Añadir un elemento al principio
conjunto.insert(0, 0)
print(f"El conjunto despues de insertar al principio es: {conjunto}")

# Añadir varios elementos al final del conjunto
conjunto.extend([7, 8, 9])
print(f"El conjunto despues de insertar multiples elementos es: {conjunto}")

# Añadir varios elementos en una posicion concreta
conjunto[3:3] = [-1, -2, -3]
print(f"El conjunto despues de insertar multiples elementos es: {conjunto}")

# Eliminar el elemento de una posicion concreta
del conjunto[0]
print(f"El conjunto despues de eliminar un elemento es: {conjunto}")

# Actualizar el elemento de una posicion concreta
conjunto[0] = -1
print(f"El conjunto despues de actualizar un elemento es: {conjunto}")

# Comprobar si un elemento esta en el conjunto
PERTENECE_CONJUNTO1 = -1 in conjunto
PERTENECE_CONJUNTO2 = -10 in conjunto
print(f"Comprobar si pertenece al conjunto: {PERTENECE_CONJUNTO1}")
print(f"Comprobar si pertenece al conjunto: {PERTENECE_CONJUNTO2}")

# Eliminar todo el contenido del conjunto
conjunto.clear()
print(f"Conjunto luego de eliminar todo el contenido: {conjunto}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA

CONJUNTO_A = {1, 2, 3, 4}
CONJUNTO_B = {3, 4, 5, 6}
print(f"Conjunto A: {CONJUNTO_A}")
print(f"Conjunto B: {CONJUNTO_B}")

# UNION
print(f"Union: {CONJUNTO_A.union(CONJUNTO_B)}")

# INTERSERCCION
print(f"Interseccion: {CONJUNTO_A.intersection(CONJUNTO_B)}")

# DIFERENCIA
print(f"Diferencia A-B: {CONJUNTO_A.difference(CONJUNTO_B)}")
print(f"Diferencia B-A: {CONJUNTO_B.difference(CONJUNTO_A)}")

# DIFERENCIA SIMETRICA
print(f"Diferencia simetrica: {CONJUNTO_A.symmetric_difference(CONJUNTO_B)}")
# -----------------------------------------------------------------------------------
