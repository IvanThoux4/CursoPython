"""Module providing a function printing python version."""

#  /*
#  * UNIDAD 29: SOLID: PRINCIPIO DE SUSTITUCION DE LISKOV (LSP)
#  * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
#  * cumplir el LSP.
#  * Instrucciones:
#  * 1. Crea la clase Vehículo.
#  * 2. Añade tres subclases de Vehículo.
#  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#  * 4. Desarrolla un código que compruebe que se cumple el LSP.
#  * /-------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# El principio de sustitucion de liskov dice que los objetos de una clase deben poder
# reemplazar a los de su clase base sin alterar el funcionamiento correcto del programa
# Esto significa que una subclase debe cumplir con el contrado de la clase base, sin
# romper sus expectativas.
# -------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Ejemplo incorrecto (rompiendo LSP)


class NoPuedoVolarError(Exception):
    """Generamos una excepcion nueva"""


class Ave:
    """Clase ave"""

    def volar(self):
        """Funcion volar"""
        return "Estoy volando"


class Pinguino(Ave):
    """Subclase: pinguino"""

    def volar(self):
        """Funcion volar"""
        # Rompe el contrato: los pinguinos no vuelan
        raise NoPuedoVolarError("No puedo volar")


def hacer_volar(ave: Ave):
    """Funcion para ejecutar el vuelo"""
    print(ave.volar())


# Ejecucion
pajaro = Ave()
hacer_volar(pajaro)  # Funciona

# pingu = Pinguino()
# hacer_volar(pingu)  # Error en tiempo de ejecucion

# Problema: Pinguino herda de Ave, pero no cumple la expectativa de que un ave pueda
# volar, lo que rompe el contrato y provoca errores.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Ejemplo correcto (cumpliendo LSP)


class EspecieAve:
    """Clase para definir cualidades comunes de un ave"""

    def comer(self):
        """Funcion: comer"""
        return "Estoy comiendo"


class AveVoladora(EspecieAve):
    """Clase para separar las aves que si vuelan"""

    def volar(self):
        """Funcion: volar"""
        return "Estoy volando"


class AveNoVoladora(EspecieAve):
    """Clase para separar las aves que no vuelan"""

    def nadar(self):
        """Funcion: nadar"""
        return "Estoy nadando"


class Cardenal(AveVoladora):
    """Hacemos herencia dentro de gaviota"""


class Pnguino(AveNoVoladora):
    """Hacewmos herencia dentro de pinguino"""

# Ejemplo de uso


def accion_volar(ave: AveVoladora):
    """Ejecutamos la accion de volar"""
    print(ave.volar())


cardenal = Cardenal()
accion_volar(cardenal)  # Funciona

pingui = Pnguino()
print(pingui.nadar())  # No rompe las expecativas

# Crear jerarquias d clases que representen de forma coherente las capacidades reales
# asegurando que toda subclase pueda ser sustituida por su superclase sin romper el
# codigo
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


class Vehiculo:
    """Clase base: vehiculos"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.velocidad = 0

    def acelerar(self, cantidad):
        """Funcion: acelerar"""
        self.velocidad += cantidad
        print(f"{self.nombre} acelera a {self.velocidad} km/h.")

    def frenar(self, cantidad):
        """Funcion: frenar"""
        self.velocidad = max(0, self.velocidad - cantidad)
        print(f"{self.nombre} frena a {self.velocidad} km/h.")


class Coche(Vehiculo):
    """Usa la misma logica que la clase base"""


class Moto(Vehiculo):
    """Usa la misma logica que la clase base"""


class Camion(Vehiculo):
    """El camion frena mas lentamente, pero sigue cumpliendo el contrato"""

    def frenar(self, cantidad):
        self.velocidad = max(0, self.velocidad - cantidad / 2)
        print(f"{self.nombre} frena lentamente a {self.velocidad} km/h.")

# ----- Comprobacion del LSP -----


def probar_vehiculo(vehiculo):
    """Funcion: probar vehiculo"""
    vehiculo.acelerar(50)
    vehiculo.frenar(20)


vehiculos = [Coche("Gol Trend"), Moto("Yamaha 150"), Camion("Volvo")]

for v in vehiculos:
    probar_vehiculo(v)

# Todas las subclases cumplen el contrato de la clase base:
#   - acelear: aumenta la velocidad
#   - frenar: disminuye la velocidad
# El camion frena mas lentamente, pero sigue respetando el comportamiento esperado
# Podemos sustituir cualquier subclase por la clase base sin romper el codigo
# -----------------------------------------------------------------------------------
