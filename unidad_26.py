"""Module providing a function printing python version."""

# /*
#  * UNIDAD 26: LOGS
#  * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
#  * un ejemplo con cada nivel de "severidad" disponible.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
#  * y listar dichas tareas.
#  * - Añadir: recibe nombre y descripción.
#  * - Eliminar: por nombre de la tarea.
#  * Implementa diferentes mensajes de log que muestren información según la
#  * tarea ejecutada (a tu elección).
#  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
#  * /------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# El modulo logging permite registrar eventos en un programa, lo cual es util para
# depuracion, monitoreo y diagnostico. Puedes configurar el formato, el nivel de
# detalle e incluso donde se guardaran los logs (consola, archivo, etc.)
# Existen cinco niveles basicos de severidad en un loggin:
# 1) DEBUG: informacion de diagnostico, detallada para depuracion
# 2) INFO: mensajes informativos de operacion normal
# 3) WARNING: señales de que algo inesperado ocurrio, pero no detiene el programa
# 4) ERROR: errores graves que impiden que una parte del programa funcione
# 5) CRITICAL: fallos muy serios que pueden detener el programa
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import time
import logging

# Configuracion basica del logging
logging.basicConfig(
    level=logging.DEBUG,  # nivel minimo que se registrara
    format="%(asctime)s - %(levelname)s - %(message)s",  # formato del mensaje
    datefmt="%Y-%m-%d %H:%M:%S"  # formato de fecha
)

# Ejemplos de logs en cada nivel
logging.debug("Este es un mensaje DEBUG: util para depuracion.")
logging.info("Este es un mensaje INFO: informacion general.")
logging.warning(
    "Este es un mensaje WARNING: algo no esperado, pero el programa continua.")
logging.error("Este es un mensaje ERROR: algo fallo.")
logging.critical("Este es un mensaje CRITICAL: fallo grave.")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------


class GestorTareas:
    """Clase para definir los metodos del gestor de tareas"""

    def __init__(self):
        self.tareas = {}
        print("\n---------------------------------------------------------------\n")
        logging.info("Gestor de tareas inicializado.")
        print("\n---------------------------------------------------------------\n")

    @staticmethod
    def medir_tiempo(func):
        """Decorador para medir tiempo de ejecucion"""

        def wrapper(self, *args, **kwargs):
            inicio = time.perf_counter()
            resultado = func(self, *args, **kwargs)
            fin = time.perf_counter()
            logging.debug(
                "Tiempo de ejecucion de '%s': %.4f segundos.", func.__name__, fin - inicio)
            return resultado
        return wrapper

    @medir_tiempo
    def aniadir_tarea(self, nombre, descripcion):
        """Funcion para añadir una tarea a la lista"""
        if nombre in self.tareas:
            logging.warning("No se añadio la tarea '%s', ya existe.", nombre)
            return
        self.tareas[nombre] = descripcion
        logging.info("Tarea '%s' añadida con exito.", nombre)

    @medir_tiempo
    def eliminar_tarea(self, nombre):
        """Funcion para eliminar una tarea de la lista"""
        if nombre not in self.tareas:
            logging.error(
                "No se pudo eliminar la tarea '%s', no existe.", nombre)
            return
        del self.tareas[nombre]
        logging.info("Tarea: '%s' eliminada exitosamente.", nombre)

    @medir_tiempo
    def listar_tareas(self):
        """Funcion para imprimir la lista de tareas"""
        if not self.tareas:
            logging.warning("No hay tareas registradas.")
            return
        logging.info("Listado de tareas: ")
        for nombre, descripcion in self.tareas.items():
            print(f"-{nombre}: {descripcion}")


# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()

    gestor.aniadir_tarea("Estudiar Python", "Repasar funciones y decoradores.")
    gestor.aniadir_tarea("Hacer ejercicio", "Caminar 30 minutos")
    gestor.listar_tareas()
    gestor.eliminar_tarea("Estudiar Python")
    gestor.listar_tareas()
    gestor.eliminar_tarea("Dormir")  # Provocamos un error
# -----------------------------------------------------------------------------------
