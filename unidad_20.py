"""Module providing a function printing python version."""

# /*
#  * UNIDAD 20: ENUMERACIONES
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
#  * /--------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# En python el tipo de dato que permite definir enumeraciones es Enum, que viene
# inlcuido en el modulo estandar "enum". Sirve para definir conjuntos de valores
# simbolicos con nombres legibles, asociados a valores constantes.

from enum import Enum
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Definimos el Enum para los dias de la semana


class DiaSemana(Enum):
    """Clase que reperesenta los dias de la semana en español"""
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Funcion que devuelve el nombre del dia segun un numero del 1 al 7


def obtener_dia(numero):
    """Funcion para obtener un dia de la semana"""
    try:
        return DiaSemana(numero).name.capitalize()
    except ValueError:
        return "Numero ingresado no valido, debe ser un numero del 1 al 7."


# Para imprimir todos los dias de la semana podemos utilizar la siguiente forma
for i in range(1, 8):
    print(f"{i} -> {obtener_dia(i)}")

# Para forzar el error de un dia que no esta dentro del rango utilizamos
print(obtener_dia(8))
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA

# Primero definimos el Enum para los diferentes estados del pedido


class EstadoPedido(Enum):
    """Clase que representa los diferentes estados del pedido"""
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGRADO = 3
    CANCELADO = 4

# Definimos una clase de pedidos para declarar las diferentes operaciones


class Pedido:
    """Clase con todas las funciones que contiene nuestro sistema de pedidos"""

    def __init__(self, identificador):
        """Inicializador de clase"""
        self.id = identificador
        self.estado = EstadoPedido.PENDIENTE  # Iniciamos el pedido una vez registrado

    def enviar(self):
        """Cambiar el estado en caso de que se envie el producto"""
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print(f"Pedido: {self.id} ha sido enviado.")
        elif self.estado == EstadoPedido.CANCELADO:
            print(f"Pedido: {self.id} no se puede enviar, ha sido cancelado.")
        else:
            print(f"Pedido: {self.id} fue enviado o entregado.")

    def entregar(self):
        """Cambiar el estado en caso de que se entregue el producto"""
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGRADO
            print(f"Pedido: {self.id} ha sido entregado.")
        elif self.estado == EstadoPedido.PENDIENTE:
            print(
                f"Pedido: {self.id} no se puede entregar debido a que no ha sido enviado.")
        elif self.estado == EstadoPedido.CANCELADO:
            print(f"Pedido: {self.id} esta cancelado, no se puede entregar.")
        else:
            print(f"Pedido: {self.id} ha sido entregado.")

    def cancelar(self):
        """Cambiar el estado en caso de que se cancele el producto"""
        if self.estado in (EstadoPedido.PENDIENTE, EstadoPedido.ENVIADO):
            self.estado = EstadoPedido.CANCELADO
            print(f"Pedido: {self.id} ha sido cancelado.")
        elif self.estado == EstadoPedido.ENTREGRADO:
            print(
                f"Pedido: {self.id} ya fue entregado, no es posible cancelar.")
        else:
            print(f"Pedido: {self.id} ya esta cancelado.")

    def descripcion_estado(self):
        """Descripcion de mensajes de estado"""
        mensajes = {
            EstadoPedido.PENDIENTE: "El pedido esta pendiente de envio.",
            EstadoPedido.ENVIADO: "El pedido ha sido enviado y esta en camino.",
            EstadoPedido.ENTREGRADO: "El pedido ha sido entregado al cliente.",
            EstadoPedido.CANCELADO: "El pedido fue cancelado."
        }
        return mensajes[self.estado]
# -----------------------------------------------------------------------------------
