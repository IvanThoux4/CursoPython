"""Module providing a function printing python version."""

# /*
#  * UNIDAD 28: SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
#  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
#  * Requisitos:
#  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
#  * Instrucciones:
#  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
#  * 2. Comprueba que el sistema funciona.
#  * 3. Agrega una quinta operación para calcular potencias.
#  * 4. Comprueba que se cumple el OCP.
#  * /---------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Las entidades de software (clases, modulos, funciones) deben estar abiertas para la
# extension, pero cerradas para la modificacion. Esto significa que debemos poder
# añadir nuevas funcionalidades sin modificar el codigo existente, solo extendiendolo
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Ejemplo incorrecto (Violando OCP): cada vez que agregamos un tipo de pago tenemos
# que modificar la clase ProcesarPago, lo cual rompe el OCP.


from abc import ABC, abstractmethod


class ProcesarPago:
    """Clase para definir diferentes metodos de pago"""

    def procesar_pago(self, metodo_pago, cantidad):
        """Funcion que contiene los metodos de pago aceptados"""
        if metodo_pago == "tarjeta_credito":
            print(f"Procesando pago con tarjeta de credito por ${cantidad}.")
        elif metodo_pago == "efectivo":
            print(f"Procesando pago en efectivo por ${cantidad}.")
        else:
            print("Metodo de pago desconocido, intente nuevamente.")


# Ejemplo de uso
procesar = ProcesarPago()
procesar.procesar_pago("tarjeta_credito", 100)
procesar.procesar_pago("efectivo", 50)

# PROBLEMA: si se quiere agregar un nuevo metodo de pago, debemos modificar la clase
# original, lo que puede romper el codigo existente.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Ejemplo correcto (cumpliendo OCP): debemos utilizar herencia y polimorfismo para
# que el sistema sea extensible sin modificar la clase base.


# Definimos primero la clase base (cerrada a modificacion, abierta a extension)

class MetodoPago(ABC):
    """Funcion base"""
    @abstractmethod
    def pagar(self, cantidad):
        """Funcion para finalizar el pago"""

# Implementaciones concretas (extensiones)


class PagoTarjetaCredito(MetodoPago):
    """Extension: pago con tarjeta de credito"""

    def pagar(self, cantidad):
        """Funcion para realizar el pago"""
        print(f"Procesando pago con tarjeta de credito por ${cantidad}.")


class PagoEfectivo(MetodoPago):
    """Extension: pago con efectivo"""

    def pagar(self, cantidad):
        """Funcion para realizar el pago"""
        print(f"Procesando pago con efectivo por ${cantidad}.")

# Nuevo metodo de pago sin tocar las clases existentes


class PagoBitcoin(MetodoPago):
    """Extension: pago con Bitcoin"""

    def pagar(self, cantidad):
        """Funcion para realizar el pago"""
        print(f"Procesando pago con bitcoin por ${cantidad}.")

# Procesador que utiliza polimorfismo


class ProcesadorPago:
    """Utilizamos polimorfismo"""

    def proceso(self, metodo_pago: MetodoPago, cantidad):
        """Utilizamos polimorfismo"""
        metodo_pago.pagar(cantidad)


# Ejemplo de uso
procesador = ProcesadorPago()
procesador.proceso(PagoTarjetaCredito(), 100)
procesador.proceso(PagoEfectivo(), 200)
procesador.proceso(PagoBitcoin(), 500)

# Ventajas de cumplir el OCP
# 1) Extensible: se añaden nuevas formas de pago sin modificar la clase MetodoPago
# 2) Mantenible: menos riesgo de romper codigo ya probado
# 3) Cumple OCP: abierto a extension, cerrado a modificacion
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA
# Interfaz para operaciones


class Operacion(ABC):
    """Clase base para operaciones"""
    @abstractmethod
    def ejecutar(self, a, b):
        """Funcion para ejecutar la operacion seleccionada"""

# Operaciones existentes


class Suma(Operacion):
    """Clase para definir suma"""

    def ejecutar(self, a, b):
        """Operacion: suma"""
        return a+b


class Resta(Operacion):
    """Clase para definir la resta"""

    def ejecutar(self, a, b):
        """Operacion: resta"""
        return a-b


class Multiplicar(Operacion):
    """Clase para definir la multiplicacion"""

    def ejecutar(self, a, b):
        """Operacion: multiplicacion"""
        return a*b


class Division(Operacion):
    """Clase para definir la division"""

    def ejecutar(self, a, b):
        """Operacion: division"""
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return a/b

# Una ves definido todo, agregamos la nueva operacion


class Potencia(Operacion):
    """Clase para definir la potencia"""

    def ejecutar(self, a, b):
        """Operacion: potencia"""
        return a ** b


class Calculadora:
    """Clase de calculadora"""

    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        """Funcion para registrar una operacion"""
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        """Funcion para ejecutar una operacion"""
        if nombre not in self.operaciones:
            raise ValueError(f"Operacion '{nombre}' no soportada.")
        return self.operaciones[nombre].ejecutar(a, b)


# Ejemplo de uso
calc = Calculadora()
calc.registrar_operacion("sum", Suma())
calc.registrar_operacion("res", Resta())
calc.registrar_operacion("mult", Multiplicar())
calc.registrar_operacion("div", Division())

print(calc.calcular("sum", 5, 3))  # Resultado = 8
print(calc.calcular("mult", 5, 3))  # Resultado = 15

# Registrar la nueva operacion
calc.registrar_operacion("pot", Potencia())
print(calc.calcular("pot", 2, 3))  # Resultado = 8

# Ventajas de este diseño
# 1) Abierto a extension -> solo agregamos nuevas clases para nuevas operaciones
# 2) Cerrado a modificacion -> Calculadora no cambia aunque sumemos operaciones
# 3) Escalable -> facil de mantener y probar
# -----------------------------------------------------------------------------------
