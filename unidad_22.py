"""Module providing a function printing python version."""

# /*
#  * UNIDAD 22: CALLBACKS
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.
#  * /----------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Un callback es una funcion que pasamos como argumento a otra funcion para
# que esta ultima la ejecute en un momento determinado.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Definimos dos funciones que podrian actuar como callbacks


import random
import time


def saludo_personalizado(nombre):
    """Funcion que realiza un saludo con un nombre recibido como parametro"""
    print(f"Hola, {nombre}! Bienvenido a este archivo de Python.")


def despedida_personalizada(nombre):
    """Funcion que realiza una despedida con un nombre recibido como parametro"""
    print(f"Adios, {nombre}! Espero hayas encontrado lo que buscabas.")

# Funcion que recibe otra funcion como argumento (callback)


def ejecutar_accion(nombre, accion_callback):
    """Funcion que recibe otra funcion y ejecuta el callback"""
    print("Ejecutando accion:")
    accion_callback(nombre)
    print("Accion finalizada.\n")


# Uso de la funcion con diferentes callbacks
ejecutar_accion("Ivan", saludo_personalizado)
ejecutar_accion("Lucas", despedida_personalizada)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


# Definimos los callbacks

def confirmar_pedido(plato):
    """Funcion para confirmar el pedido"""
    print(f"Pedido confirmado: {plato}.")


def plato_listo(plato):
    """Funcion para informar que el plato se encuentra listo"""
    print(f"El plato: {plato}, esta listo para servir.")


def entregar_pedido(plato):
    """Funcion para entregar el pedido"""
    print(f"Pedido entregado: {plato}.")

# Funcion principal que procesa el pedido


def procesar_pedido(plato, callback_confirmacion, callback_listo, callback_entregar):
    """Funcion que procesa los diferentes estados del pedido"""
    # Confirmar pedido
    callback_confirmacion(plato)
    time.sleep(random.randint(1, 10))  # Simulamos el tiempo de preparacion

    # Plato listo
    callback_listo(plato)
    time.sleep(random.randint(1, 10))  # Simulamos el tiempo de entrega

    # Entregar pedido
    callback_entregar(plato)


# Ejemplo de uso
if __name__ == "__main__":
    print("\n-------------------------------------------\n")
    procesar_pedido("Pizza Napolitana", confirmar_pedido,
                    plato_listo, entregar_pedido)
    print("\n-------------------------------------------\n")
    procesar_pedido("Hamburguesa c/ papas fritas",
                    confirmar_pedido, plato_listo, entregar_pedido)
    print("\n-------------------------------------------\n")

# -----------------------------------------------------------------------------------
