"""Module providing a function printing python version."""

# /*
#  * UNIDAD 30: SOLID: PRINCIPIO DE SEGREGACION DE INTERFACES (ISP)
#  * Explora el "Principio SOLID de Segregación de Interfaces
#  * (Interface Segregation Principle, ISP)", y crea un ejemplo
#  * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un gestor de impresoras.
#  * Requisitos:
#  * 1. Algunas impresoras sólo imprimen en blanco y negro.
#  * 2. Otras sólo a color.
#  * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
#  * Instrucciones:
#  * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
#  * 2. Aplica el ISP a la implementación.
#  * 3. Desarrolla un código que compruebe que se cumple el principio.
#  * /-----------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# El principio de segregacion de interfaces dice que una clase no debe verse obligada a
# implementar interfaces que no utilice. En otras palabras, es mejor tener interfaces
# pequeñas y especifica que una gigante con metodos que algunas clases no necesitan
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Ejemplo incorrecto (violando ISP)
from abc import ABC, abstractmethod


class Animal(ABC):
    """Clase para definir a un animal"""
    @abstractmethod
    def comer(self):
        """Funcion: comer"""

    @abstractmethod
    def volar(self):
        """Funcion: volar"""

    @abstractmethod
    def nadar(self):
        """Funcion: nadar"""


class Perro(Animal):
    """Clase: perro hereda cualidades de clase animal"""

    def comer(self):
        """Funcion: comer"""
        print("El perro come croquetas.")

    def volar(self):
        """Funcion: volar"""
        raise NotImplementedError(
            "El perro no puede volar.")  # Los perros no pueden volar

    def nadar(self):
        """Funcion: nadar"""
        print("El perro nada en la piscina.")
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Ejemplo correcto (Cumpliendo ISP)
# Desarrollamos interfaces pequeñas y especificas


class PuedeComer(ABC):
    """Clase: desarrollamos una accion para comer"""
    @abstractmethod
    def comer(self):
        """Funcion: comer"""


class PuedeVolar(ABC):
    """Clase: desarrollamos una accion para volar"""
    @abstractmethod
    def volar(self):
        """Funcion: volar"""


class PuedeNadar(ABC):
    """Clase: desarrollamos una accion para nadar"""
    @abstractmethod
    def nadar(self):
        """Funcion: nadar"""


class Dog(PuedeComer, PuedeNadar):
    """Clase perro hereda los metodos nadar y comer"""

    def comer(self):
        """Funcion: comer"""
        print("El perro come croquetas.")

    def nadar(self):
        """Funcion: nadar"""
        print("El perro nada en la piscina.")


class Bird(PuedeComer, PuedeVolar):
    """Clase pajaro hereda los metodos comer y volar"""

    def comer(self):
        """Funcion: comer"""
        print("El pajaro come semillas.")

    def volar(self):
        """Funcion: volar"""
        print("El pajaro vuela alto.")


class Duck(PuedeComer, PuedeNadar, PuedeVolar):
    """Clase pato hereda los metodos comer, nadar y volar"""

    def comer(self):
        """Funcion: comer"""
        print("El pato come hierbas acuaticas.")

    def volar(self):
        """Funcion: volar"""
        print("El pato vuela distancias cortas.")

    def nadar(self):
        """Funcion: nadar"""
        print("El pato nada en el lago.")

# Cada clase implementa solo lo que necesita. Permite una mayor flexibilidad y es mas
# facil realizar mantenimiento. Evita metodos inutiles o excepciones innecsearias.
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# DESAFIO EXTRA


class PuedeImprimirBN(ABC):
    """Clase que implementa la impresion en blanco y negro"""
    @abstractmethod
    def imprimir_bn(self):
        """Funcion: imprimir en blanco y negro"""


class PuedeImprimirColor(ABC):
    """Clase que implementa la impresion en color"""
    @abstractmethod
    def imprimir_color(self):
        """Funcion: imprimir en color"""


class PuedeEscanear(ABC):
    """Clase que implementa el escaneo de archivos/materiales"""
    @abstractmethod
    def escanear(self):
        """Funcion: escanear"""


class PuedeEnviarFax(ABC):
    """Clase que implementa el envio de Fax"""
    @abstractmethod
    def enviar_fax(self):
        """Funcion: enviar fax"""

# Implementaciones concretas:


class ImpresoraBN(PuedeImprimirBN):
    """Clase impresora en blanco y negro"""

    def imprimir_bn(self):
        print("Imprimiendo en blanco y negro...")


class ImpresoraColor(PuedeImprimirColor):
    """Clase impresora en color"""

    def imprimir_color(self):
        print("Imprimiendo en color...")


class ImpresoraMultifuncion(PuedeImprimirBN, PuedeImprimirColor, PuedeEscanear, PuedeEnviarFax):
    """Clase impresora multifuncion"""

    def imprimir_bn(self):
        print("Imprimiendo en blanco y negro...")

    def imprimir_color(self):
        print("Imprimiendo en color...")

    def escanear(self):
        print("Escaneando archivo/material...")

    def enviar_fax(self):
        print("Enviando fax...")


if __name__ == "__main__":
    # Solo blanco y negro
    byn = ImpresoraBN()
    byn.imprimir_bn()

    # Solo a color
    color = ImpresoraColor()
    color.imprimir_color()

    # Multifuncion
    multi = ImpresoraMultifuncion()
    multi.imprimir_bn()
    multi.imprimir_color()
    multi.escanear()
    multi.enviar_fax()

# Cada impresora solo implementa las funcionalidades que necesita.
# Agregar una nueva impresora con funciones especificas no obliga modificar el codigo
# existente
# -------------------------------------------------------------------------------------
