"""Module providing a function printing python version."""

# /*
#  * UNIDAD 27: SOLID: PRINCIPIO DE RESPONSABILIDAD UNICA (SRP)
#  * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
#  * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
#  * información básica como título, autor y número de copias disponibles.
#  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  * información básica como nombre, número de identificación y correo electrónico.
#  * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  * tomar prestados y devolver libros.
#  * Instrucciones:
#  * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
#  * los tres aspectos mencionados anteriormente (registro de libros, registro de
#  * usuarios y procesamiento de préstamos).
#  * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
#  * siguiendo el Principio de Responsabilidad Única.
#  * /------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# El Single Responsibility Principle dice que una clase debe tener una sola razon
# para cambiar, es decir, debe encargarse de una sola cosa. Si una clase mezcla
# responsabilidades, es mas dificil de mantener, probar y extender.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# EJEMPLO INCORRECTO (viola el principio SRP)
import os


class ManejadorDeReportes:
    """Clase de para manejar reportes"""

    def __init__(self, dato):
        self.dato = dato

    def generar_reporte(self):
        """Funcion para generar el contenido del reporte"""
        return f"Reporte: {self.dato}"

    def guardar_archivo(self, nombre_archivo):
        """Funcion para guardar el contenido dentro del reporte"""
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(self.generar_reporte())

    def enviar_email(self, email):
        """Funcion para enviar un reporte a un email"""
        print(f"Enviando reporte a {email}...")


# Los problemas que presenta la clase son los siguientes: genera el reporte
# guarda el reporte en un archivo y ademas envia el reporte por email.
# Existen tres razones para cambiar -> formato del reporte, almacenamiento, envio.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# EJEMPLO CORRECTO (cumple el principio SRP)


class Reporte:
    """Clase reporte"""

    def __init__(self, dato):
        self.dato = dato

    def generar(self):
        """Funcion generar"""
        return f"Reporte: {self.dato}"


class GuardarArchivo:
    """Clase guardar archivo"""

    def guardar_archivo(self, repo, nombre_archivo):
        """Funcion guardar archivo"""
        with open(nombre_archivo, "w", encoding="utf-8") as fi:
            fi.write(repo)


class EnviarReporte:
    """Clase enviar reporte"""

    def enviar_email(self, rep, email):
        """Funcion enviar reporte a traves de email"""
        print(f"Enviando {rep} a {email}...")


# Uso
reporte = Reporte("Ventas de Agosto")
REPORTE_GENERADO = reporte.generar()

# Guardar
guardado = GuardarArchivo()
guardado.guardar_archivo(REPORTE_GENERADO, "reporte.txt")

# Enviar
enviador = EnviarReporte()
enviador.enviar_email(REPORTE_GENERADO, "cliente@hotmail.com")

os.remove("reporte.txt")

# Cada clase tiene una sola responsabilidad, lo cual facilita la mantencion y las pruebas
# Reporte -> Generar el reporte
# GuardarArchivo -> Guardar en archivo
# EnviarReporte -> Enviar por email
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA

# Primero hacemos la version que no cumple con el SRP, donde la clase libreria se
# encarga de demasiadas cosas a la vez, registrar libros, usuarios y procesar prestamos


class Libreria:
    """Clase libreria que no cumple el SRP"""

    def __init__(self):
        self.libros = {}
        self.clientes = {}
        self.prestamos = []

    def agregar_libro(self, nombre_libro, autor, cantidad):
        """Funcion para añadir un libro nuevo"""
        self.libros[nombre_libro] = {"Autor": autor, "Cantidad": cantidad}

    def agregar_cliente(self, nombre, nombre_usuario, email):
        """Funcion para añadir un cliente de la libreria"""
        self.clientes[nombre_usuario] = {"Nombre": nombre, "E-mail": email}

    def cargar_prestamo(self, nombre_usuario, nombre_libro):
        """Funcion para cargar un nuevo prestamo del libro"""
        if nombre_libro in self.libros and self.libros[nombre_libro]["Cantidad"] >= 0:
            self.libros[nombre_libro]["Cantidad"] -= 1
            self.prestamos.append(
                {"NombreUsuario": nombre_usuario, "NombreLibro": nombre_libro})
            print(
                f"{nombre_libro} prestado a {self.clientes[nombre_usuario]['Nombre']}")

    def regresar_prestamo(self, nombre_usuario, nombre_libro):
        """Funcion para cargar el retorno del libro prestado"""
        for prestamo in self.prestamos:
            if prestamo["NombreUsuario"] == nombre_usuario:
                if prestamo["NombreLibro"] == nombre_libro:
                    self.libros[nombre_libro]["Cantidad"] += 1
                    self.prestamos.remove(prestamo)
                    print(
                        f"{nombre_libro} devuelto por {self.clientes[nombre_usuario]['Nombre']}")
                    return
            print("Prestamo no encontrado")


# Ejemplo de uso
lib = Libreria()
lib.agregar_libro("1984", "George Orwell", 3)
lib.agregar_cliente("Ivan Ezequiel Thoux", 1, "thouxivan@gmail.com")
lib.cargar_prestamo(1, "1984")
lib.regresar_prestamo(1, "1984")

# Si hay que cambiar la forma de registrar usuarios, el prestamo o almacenamiento de
# libros, debemos modificar la misma clase, rompiendo el principio de alta cohesion
# y bajo acoplamiento.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA

# Ahora separamos en clases con responsabilidades unicas, Gestion de libros, Gestion
# de usuarios y Gestion de prestamos, para cumplir correctamente con el SRP.


class GestionLibros:
    """Clase para gestionar los libros"""

    def __init__(self):
        self.libros = {}

    def agregar_libro(self, nombre_libro, autor, cantidad):
        """Agregar libro nuevo"""
        self.libros[nombre_libro] = {"Autor": autor, "Cantidad": cantidad}

    def esta_disponible(self, nombre_libro):
        """Retornar si esta disponible un libro"""
        return nombre_libro in self.libros and self.libros[nombre_libro]["Cantidad"] > 0

    def pedir_prestado(self, nombre_libro):
        """Pedir prestado un libro"""
        if self.esta_disponible(nombre_libro):
            self.libros[nombre_libro]["Cantidad"] -= 1
            return True
        return False

    def devolver_libro(self, nombre_libro):
        """Devolver libros"""
        if nombre_libro in self.libros:
            self.libros[nombre_libro]["Cantidad"] += 1


class GestionUsuarios:
    """Clase para gestionar usuarios"""

    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre_completo, id_usuario, email):
        """Agregar un nuevo usuario"""
        self.usuarios[id_usuario] = {
            "Nombre": nombre_completo, "Email": email}

    def obtener_usuario(self, id_usuario):
        """Buscar un usuario por su identificador"""
        return self.usuarios.get(id_usuario)


class GestionPrestamos:
    """Gestion de prestamos de libros"""

    def __init__(self, gestion_libros, gestion_usuarios):
        self.prestamos = []
        self.gestion_libros = gestion_libros
        self.gestion_usuarios = gestion_usuarios

    def prestar_libro(self, id_usuario, nombre_libro):
        """Prestar un libro y descontar su cantidad disponible"""
        usuario = self.gestion_usuarios.obtener_usuario(id_usuario)
        if usuario and self.gestion_libros.pedir_prestado(nombre_libro):
            self.prestamos.append(
                {"IDUsuario": id_usuario, "NombreLibro": nombre_libro})
            print(f"{nombre_libro} prestado a {usuario['Nombre']}.")
        else:
            print("Libro no disponible o usuario no encontrado.")

    def devolver_libro(self, id_usuario, nombre_libro):
        """Devolver libro prestado e incrementar su cantidad"""
        for prestamo in self.prestamos:
            if prestamo["IDUsuario"] == id_usuario:
                if prestamo["NombreLibro"] == nombre_libro:
                    self.gestion_libros.devolver_libro(nombre_libro)
                    self.prestamos.remove(prestamo)
                    usuario_prestamo = self.gestion_usuarios.obtener_usuario(id_usuario)[
                        'Nombre']
                    print(
                        f"{nombre_libro} devuelto por {usuario_prestamo}")
                    return
        print("Prestamo no encontrado.")


# Ejemplo de uso
libros = GestionLibros()
usuarios = GestionUsuarios()
prestamos = GestionPrestamos(libros, usuarios)

libros.agregar_libro("1984", "George Orwell", 3)
usuarios.agregar_usuario("Ivan Ezequiel Thoux", 1, "thouxivan@gmail.com")
prestamos.prestar_libro(1, "1984")
prestamos.devolver_libro(1, "1984")

# Ventajas de la version correcta
# 1) Alta cohesion: cada clase tiene una unica responsabilidad
# 2) Bajo acoplamiento: podemos cambiar una gestion sin modificar otra
# 3) Facilidad de mantenimiento y escalabilidad
# -----------------------------------------------------------------------------------
