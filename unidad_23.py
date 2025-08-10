"""Module providing a function printing python version."""

# /*
#  * UNIDAD 23: FUNCIONES DE ORDEN SUPERIOR
#  * Explora el concepto de funciones de orden superior en tu lenguaje
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
#  * lista de calificaciones), utiliza funciones de orden superior para
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
#  * /----------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Las funciones de orden superior son aquellas que pueden recibir una o mas funciones
# como argumentos, o tambien devolver una funcion como resultado
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion que recibe otra funcion como argumento


from datetime import datetime


def aplicar_operacion(x, y, operacion):
    """Recibe dos variables y una operacion, retora la operacion realizada con las variables"""
    return operacion(x, y)


def sumar(a, b):
    """Funcion para sumar dos valores"""
    return a+b


def multiplicar(a, b):
    """Funcion para multiplicar dos valores"""
    return a*b


# Ejemplos de uso
print(aplicar_operacion(5, 3, sumar))  # Retorna como resultado 8
print(aplicar_operacion(5, 3, multiplicar))  # Retorna como resultado 15
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion que devuelve otra funcion


def crear_multiplicador(n):
    """Funcion que devuelve otra funcion"""
    def multiplicar_por(valor):
        """Funcion que multiplica dos valores"""
        return valor * n
    return multiplicar_por


# Ejemplos de uso
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(10))  # Retorna como resultado 20
print(triplicar(10))  # Retorna como resultado 30
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Combinacion de ambos conceptos


def procesar_lista(lista, funcion):
    """Funcion que recibe una lista y una funcion, retorna el resultado de la funcion aplicada"""
    return [funcion(x) for x in lista]


NUMEROS = [1, 2, 3, 4, 5]

# Utilizamos funciones lambda
# Retorna como resultado [1, 4, 9, 16, 25]
print(procesar_lista(NUMEROS, lambda x: x ** 2))
# Retorna como resultado [11, 12, 13, 14, 15]
print(procesar_lista(NUMEROS, lambda x: x + 10))
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


# Creamos una lista de estudiantes
estudiantes = [
    ("Ivan", "1999-07-05", [9.5, 8.7, 10]),
    ("Luis", "2001-09-22", [7.5, 6.8, 8]),
    ("Pedro", "2004-01-10", [9.2, 9.8, 10]),
    ("Juan", "2002-07-30", [5.5, 7, 6.8]),
    ("Esteban", "2000-12-02", [8.5, 9, 9.5])
]

# Validamos que las calificaciones esten entre 0 y 10

for nombre, _, calificacion in estudiantes:
    if not all(0 <= c <= 10 for c in calificacion):
        raise ValueError(
            f"Calificaciones invalidas para el estudiante: {nombre}.")

# Calculamos el promedio de calificaciones
promedios = list(map(
    lambda e: (e[0], round(sum(e[2]) / len(e[2]), 2)),
    estudiantes
))

# Mejores estudiantes (promedio >= 9)
mejores = list(map(
    lambda e: e[0],
    filter(lambda e: sum(e[2]) / len(e[2]) >= 9, estudiantes)
))

# Ordenar desde mas joven a mas viejo
orden_nacimiento = list(map(
    lambda e: e[0],
    sorted(estudiantes, key=lambda e: datetime.strptime(
        e[1], "%Y-%m-%d"), reverse=True)
))

# Mayor calificacion de todas
mayor_calificacion = max(map(lambda e: max(e[2]), estudiantes))

# Mostramos los resultados en la terminal
print(f"Promedios: {promedios}")
print(f"Mejores estudiantes: {mejores}")
print(f"Ordenar de mas joven a mas viejo: {orden_nacimiento}")
print(f"Mayor calificacion obtenida: {mayor_calificacion}")
# -----------------------------------------------------------------------------------
