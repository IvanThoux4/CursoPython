"""Module providing a function printing python version."""

# /*
#  * UNIDAD 9:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parametros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  * /----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONCEPTO DE CLASE
# Una clase es una plantilla para crear objetos. Define atributos y métodos que
# los objetos creados a partir de la clase tendran.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CARACTERISTICAS A IMPLEMENTAR
# - Inicializador: Método especial que se llama al crear una instancia de la clase.
# - Atributos: Variables que pertenecen a la clase.
# - Método para imprimir los atributos.
# - Creación de una instancia, modificación de atributos e impresión.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------


class Persona:
    """Clase que representa a una persona."""

    def __init__(self, nombre, edad, ciudad):
        """Inicializador de la clase Persona."""
        self.nombre = nombre  # Atributo nombre
        self.edad = edad     # Atributo edad
        self.ciudad = ciudad  # Atributo ciudad

    def mostrar_datos(self):
        """Imprime los datos de la persona."""
        print("--------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")
        print("--------------------------")


# Crear una instancia de la clase
persona1 = Persona("Juan", 30, "Madrid")

# Mostrar los datos de la persona
persona1.mostrar_datos()

# Modificar los atributos de la persona
persona1.nombre = "Juan"
persona1.edad = 31
persona1.ciudad = "Barcelona"

# Imprimir los datos modificados
persona1.mostrar_datos()

# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA
# Pilas


class NavegadorWeb:
    """Simula un navegador web con funcionalidades de adelante/atrás usando una pila."""

    def __init__(self):
        """Inicializa el historial de navegación."""
        self.historial = []

    def cargar_url(self, url):
        """Carga una nueva URL en el historial."""
        self.historial.append(url)

    def atras(self):
        """Navega a la página anterior."""
        if self.contar() == 0:
            print("No hay paginas anteriores en el historial.")
            return
        return self.historial.pop()

    def contar(self):
        """Retorna el número de páginas en el historial."""
        return len(self.historial)

    def mostrar_historial(self):
        """Imprime el historial de navegación."""
        if self.contar() == 0:
            print("No hay historial de navegacion.")
            return
        else:
            print("Historial de navegación:")
            for url in self.historial:
                print(url)


navegador_web = NavegadorWeb()
navegador_web.cargar_url("https://www.ejemplo1.com")
navegador_web.cargar_url("https://www.ejemplo2.com")
navegador_web.cargar_url("https://www.ejemplo3.com")
print(navegador_web.contar())
navegador_web.mostrar_historial()
navegador_web.atras()
print(navegador_web.contar())
print(navegador_web.atras())
print(navegador_web.atras())
print(navegador_web.atras())
print(navegador_web.atras())
print(navegador_web.atras())
print(navegador_web.contar())

# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA
# Colas


class ColaImpresion:
    """Simula una cola de impresión compartida."""

    def __init__(self):
        """Inicializa la cola de impresión."""
        self.cola_impresion = []

    def agregar_elemento(self, archivo):
        """Agrega un archivo a la cola de impresión."""
        self.cola_impresion.append(archivo)

    def imprimir_elemento(self):
        """Imprime el siguiente archivo en la cola de impresión."""
        if self.contar() == 0:
            print("No hay documentos en la cola de impresion para imprimir.")
            return
        return self.cola_impresion.pop(0)

    def contar(self):
        """Retorna el número de elementos en la cola de impresión."""
        return len(self.cola_impresion)

    def mostrar_elementos(self):
        """Imprime todos los elementos en la cola de impresión."""
        for elemento in self.cola_impresion:
            print(elemento)


cola_impresion = ColaImpresion()
cola_impresion.agregar_elemento("Documento A")
cola_impresion.agregar_elemento("Documento B")
cola_impresion.agregar_elemento("Documento C")
print(cola_impresion.contar())
cola_impresion.mostrar_elementos()
cola_impresion.imprimir_elemento()
print(cola_impresion.contar())
cola_impresion.imprimir_elemento()
cola_impresion.imprimir_elemento()
cola_impresion.imprimir_elemento()
cola_impresion.imprimir_elemento()
print(cola_impresion.contar())
# -----------------------------------------------------------------------------------
