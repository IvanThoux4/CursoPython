"""Module providing a function printing python version."""

# /*
#  * UNIDAD 24: PATRONES DE DISEÑO: SINGLETON
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.
#  * /--------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# El patron de diseño Singleton asegura que solo exista una instancia de una clase
# durante la ejecucion del programa, y que se pueda acceder a ella desde cualquier
# parte. En Python la forma de implementarlo es usando el control '__new__'
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------


class Singleton:
    """Definicion de clase para implementar el patron de diseño"""
    _instancia = None  # Variable de la clase para guardar la unica instancia

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            print("Creando nueva instancia...")
            cls._instancia = super().__new__(cls)
        else:
            print("Usando la instancia existente.")
        return cls._instancia

    def __init__(self, valor):
        self.valor = valor


# Probamos el Singleton
INSTANCIA_1 = Singleton("Primero")
print("Instancia 1: ", INSTANCIA_1.valor)

INSTANCIA_2 = Singleton("Segundo")
print("Instancia 2: ", INSTANCIA_2.valor)

print("¿Es la misma instancia?: ", INSTANCIA_1 is INSTANCIA_2)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


class SesionUsuario:
    """Definimos una clase que contendra los metodos y datos del usuario"""
    _instancia = None  # Guardar una unica instancia

    def __new__(cls):
        if cls._instancia is None:
            print("Creando nueva instancia...")
            cls._instancia = super().__new__(cls)
        else:
            print("Ustando la sesion existente.")
        return cls._instancia

    def __init__(self):
        if not hasattr(self, 'usuario'):
            self.usuario = None

    def asignar_usuario(self, identificador, nombreusuario, nombre, email):
        """Funcion para crear una instancia del usuario con los datos"""
        self.usuario = {
            "id": identificador,
            "nombreusuario": nombreusuario,
            "nombre": nombre,
            "email": email
        }
        print(f"Usuario: '{nombreusuario}' asignado a la sesion actual.")

    def obtener_usuario(self):
        """Funcion para obtener el usuario asignado a una sesion"""
        if self.usuario:
            return self.usuario
        else:
            print("No hay usuario registrado en la sesion.")
            return None

    def borrar_sesion(self):
        """Funcion para quitar el usuario asignado a la sesion."""
        self.usuario = None
        print("Sesion eliminada.")


# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una primer instancia
    sesion1 = SesionUsuario()
    sesion1.asignar_usuario(
        1, "Ivan22", "Ivan Ezequiel Thoux", "thouxivan@gmail.com")

    # Creamos una segunda instancia (en realidad es la misma instancia)
    sesion2 = SesionUsuario()

    print(f"\nDatos de la sesion 2: {sesion2.obtener_usuario()}")

    # Borramos la sesion 2
    sesion2.borrar_sesion()

    # Comprobamos los datos de la sesion 1
    print(f"\nDatos de la sesion 1: {sesion1.obtener_usuario()}")

    # Verificar si son la misma instancia
    print(f"¿Es la misma instancia?: {sesion1 is sesion2}")
# -----------------------------------------------------------------------------------
