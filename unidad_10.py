"""Module providing a function printing python version."""

# /*
#  * UNIDAD 10:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  * /--------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# SUPERCLASE


class Animal:
    """Clase base para representar un animal."""

    def __init__(self, nombre):
        """Inicializa el animal con un nombre."""
        self.nombre = nombre

    def hacer_sonido(self):
        """Método que devuelve un sonido genérico de animal."""
        return "Sonido de animal"

# SUBCLASE PERRO


class Perro(Animal):
    """Clase que representa un perro, hereda de Animal."""

    def hacer_sonido(self):
        """Método que devuelve el sonido específico de un perro."""
        return "Guau Guau"

# SUBCLASE GATO


class Gato(Animal):
    """Clase que representa un gato, hereda de Animal."""

    def hacer_sonido(self):
        """Método que devuelve el sonido específico de un gato."""
        return "Miau Miau"

# Funcion para imprimir los sonidos de los animales


def imprimir_sonido(animal):
    """Imprime el sonido que hace un animal."""
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")


# Crear instancias de las clases
animal_generico = Animal("Animal XX")  # Instancia de la superclase
perro = Perro("Firulais")
gato = Gato("Michi")

# Imprimir sonido de los animales con la funcion
imprimir_sonido(animal_generico)
imprimir_sonido(perro)
imprimir_sonido(gato)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA: Empresa de desarrollo


class Empleado:
    """Clase base para representar un empleado en la empresa."""

    def __init__(self, identificador: int, nombre: str):
        """Inicializa el empleado con un identificador y un nombre."""
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []

    def aniadir_empleado(self, empleado):
        """Añade un empleado a la lista de empleados a cargo."""
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        """Muestra los nombres de los empleados a cargo."""
        for empleado in self.empleados:
            print(empleado.nombre)


class Gerente(Empleado):
    """Clase que representa a un gerente, hereda de Empleado."""

    def coordinar_proyectos(self):
        """Método que permite al gerente coordinar todos los proyectos de la empresa."""
        print(f"{self.nombre} esta coordinando todos los proyectos de la empresa.")


class GerenteDeProyecto(Empleado):
    """Clase que representa a un gerente de proyecto, hereda de Empleado."""

    def __init__(self, identificador, nombre, proyecto):
        """Inicializa el gerente de proyecto con un identificador, nombre y proyecto."""
        super().__init__(identificador, nombre)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        """Método que permite al gerente de proyecto coordinar su proyecto específico."""
        print(f"{self.nombre} esta coordinando su proyecto.")


class Programador(Empleado):
    """Clase que representa a un programador, hereda de Empleado."""

    def __init__(self, identificador, nombre, lenguage):
        """Inicializa el programador con un identificador, nombre y lenguaje de programación."""
        super().__init__(identificador, nombre)
        self.lenguage = lenguage

    def codigo(self):
        """Método que permite al programador escribir código en su lenguaje."""
        print(f"{self.nombre} esta programando en {self.lenguage}.")

    def agregar(self, empleado: Empleado):
        """Añade un empleado a la lista de empleados a cargo."""
        print(
            f"Un programador no tiene empleados a su cargo. {empleado.nombre} no se añadira.")


mi_gerente = Gerente(1, "Ivan Ezequiel Thoux")
mi_gerente_proyecto = GerenteDeProyecto(2, "Lucas Andres Thoux", "Proyecto 1")
mi_gerente_proyecto2 = GerenteDeProyecto(
    3, "Sandro Vicente Thoux", "Proyecto 2")
mi_programador = Programador(4, "Kontrol", "Swift")
mi_programador2 = Programador(5, "Ros", "Cobol")
mi_programador3 = Programador(6, "Bushi", "Dart")
mi_programador4 = Programador(7, "Nasos", "Python")

mi_gerente.aniadir_empleado(mi_gerente_proyecto)
mi_gerente.aniadir_empleado(mi_gerente_proyecto2)

mi_gerente_proyecto.aniadir_empleado(mi_programador)
mi_gerente_proyecto.aniadir_empleado(mi_programador2)
mi_gerente_proyecto2.aniadir_empleado(mi_programador3)
mi_gerente_proyecto2.aniadir_empleado(mi_programador4)

# Mostrará que no se puede añadir
mi_programador.aniadir_empleado(mi_programador2)

mi_programador.codigo()
mi_gerente_proyecto.coordinar_proyecto()
mi_gerente.coordinar_proyectos()
print("Empleados a cargo del gerente:")
mi_gerente.mostrar_empleados()
print("Empleados a cargo del gerente de proyecto 1:")
mi_gerente_proyecto.mostrar_empleados()
print("Empleados a cargo del programador:")
mi_programador.mostrar_empleados()
