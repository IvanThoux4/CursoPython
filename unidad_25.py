"""Module providing a function printing python version."""

# /*
#  * UNIDAD 25: PATRONES DE DISEÑO: DECORADORES
#  * Explora el concepto de "decorador" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un decorador que sea capaz de contabilizar cuántas veces
#  * se ha llamado a una función y aplícalo a una función de tu elección.
#  * /---------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Un decorador es una funcion que envuelve a otra funcion para añadirle o modificar
# su comportamiento sin cambiar su codigo original. En otras palabras, podemos decir
# que es una funcion que recibe como argumento una funcion y devuelve otra funcion
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Definicion de un decorador


def mi_decorador(funcion):
    """Funcion que representa un decorador"""
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la funcion.")
        resultado = funcion(*args, **kwargs)
        print("Despues de aplicar la funcion.")
        return resultado
    return wrapper

# Uso del decorador


@mi_decorador
def saludar(nombre):
    """Funcion para saludar al nombre que recibe como argumento"""
    print(f"Hola, {nombre}!")


# Llamada a la funcion decorada
saludar("Ivan")

# mi_decorador recibe como argumento la funcion 'saludar'
# Dentro de mi_decorador, definimos wrapper, que:
#   1) Ejecuta codigo antes de llamar a la funcion original
#   2) Llama a la funcion original (funcion(*args, **kwargs))
#   3) Ejecuta codigo despues
# El uso de @mi_decorador es equivalente a saludar = mi_decorador(saludar)
# Cuando llamamos a saludar("Ivan"), en realidad estamos llamando a wrapper
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


def contador_llamadas(funcion):
    """Funcion con decorador para contar la cantidad de veces de llamadas a la funcion"""
    llamadas = 0  # Variable para contar

    def wrapper(*args, **kwargs):
        nonlocal llamadas
        llamadas += 1
        print(f"Llamada # {llamadas} a la funcion '{funcion.__name__}'")
        return funcion(*args, **kwargs)
    return wrapper

# Aplicamos el decorador


@contador_llamadas
def saludo(nombre):
    """Funcion para saludar a una persona"""
    print(f"Hola {nombre}.")


# Ejemplos
saludo("1")
saludo("2")
saludo("3")
# -----------------------------------------------------------------------------------
