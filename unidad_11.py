"""Module providing a function printing python version."""

# /*
#  * UNIDAD 11:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado.
#  * /-------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# MANEJO DE EXCEPCIONES EN PYTHON

# Division por cero
try:
    resultado = 10/0
except ZeroDivisionError as e:
    print("¡Error atrapado! No se puede dividir por cero.")
    print(f"Detalles del error: {e}")

# Acceder a un indice inexistente
LISTA = [1, 2, 3]
try:
    elemento = LISTA[10]
except IndexError as e:
    print("¡Error atrapado! Indice fuera de rango.")
    # print(f"Detalles del error: {e}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA: Manejo de excepciones personalizadas


# Excepcion personalizada
class ValorNegativoError(Exception):
    """Exepcion lanzada cuando el valor es negativo."""


def procesar_datos(valor):
    """Funcion para capturar una excepcion"""
    if not isinstance(valor, int):
        # 'raise' se utiliza para provocar una excepcion de manera explicita.
        # Cuando se encuenta un raise se detiene la ejecicion del bloque de codigo
        # y se busca un manejador de excepciones que capture el tipo de error lanzado.
        raise TypeError("El valor debe ser un numero entero.")
    if valor == 0:
        raise ZeroDivisionError("El Valor no puede ser cero.")
    if valor < 0:
        raise ValorNegativoError("No se permiten valores negativos.")

    resultados = 100 / valor
    print(f"Resultado del calculo: {resultados}.")


# Llamada a la funcion y manejo de excepciones
try:
    dato = int(input("Ingrese un numero entero: "))
    procesar_datos(dato)
except (TypeError, ZeroDivisionError, ValorNegativoError) as e:
    print(f"Se produjo un error: {type(e).__name__}: {e}")
else:
    print("La funcion se ejecuto correcamente, sin errores.")
finally:
    print("La ejecucion finalizo.")
# -----------------------------------------------------------------------------------
