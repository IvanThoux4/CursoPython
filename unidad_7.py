"""Module providing a function printing python version."""

# /*
#  * UNIDAD 7:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  * /-------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# PILAS

pila = []

# Agregar elementos a la pila
pila.append("A")
pila.append("B")
pila.append("C")
print(f"Pila despues de agregar elementos: {pila}")

# Sacar elementos de la pila
ultimo = pila.pop()
print(f"Elemento sacado de la pila: {ultimo}")
print(f"Pila despues de sacar un elemento: {pila}")

# Ver elemento en la cima sin retirarlo (PEEK)
if pila:
    cima = pila[-1]
    print(f"Elemento en la cima de la pila: {cima}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# COLAS

cola = []

# Agregar elementos a la cola
cola.append("A")
cola.append("B")
cola.append("C")
print(f"Cola despues de agregar elementos: {cola}")

# Recupearar el primer elemento de la cola
primero = cola.pop(0)
print(f"Elemento recuperado de la cola: {primero}")
print(f"Cola despues de recuperar un elemento: {cola}")

# Ver el primer elemento de la cola sin retirarlo (PEEK)
if cola:
    inicio = cola[0]
    print(f"Elemento al inicio de la cola: {inicio}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA


# Navegador web simulado con pila
def navegador_web():
    historial = []
    utilizado = 0

    while True:
        accion = input(
            "Ingrese una acción (adelante, atras, salir o nombre de web): ")
        if accion == "salir":
            print("Saliendo del navegador.")
            break
        elif accion == "atras":
            if len(historial) > 1:
                pagina_atras = historial.pop()
                utilizado += 1
            else:
                print("No hay páginas anteriores en el historial.")
        elif accion == "adelante":
            if utilizado > 0:
                utilizado -= 1
                historial.append(pagina_atras)
            else:
                print("No hay páginas adelante en el historial.")
                pass
        else:
            historial.append(accion)

        if len(historial) > 0:
            url_completa = "/".join(historial)
            print(f"Has navegado a la web: {url_completa}")
        else:
            print("No hay historial de navegación.")


navegador_web()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA


# Impresora compartida simulada con cola

def cola_de_impresion():

    cola_impresion = []

    while True:
        accion = input(
            "Ingrese un documento para imprimir, 'imprimir' para imprimir el siguiente documento o 'salir' para salir: ")

        if accion == "salir":
            print("Saliendo de la cola de impresion.")
            break
        elif accion == "imprimir":
            if len(cola_impresion) > 0:
                documento = cola_impresion.pop(0)
                print(f"Imprimiendo documento: {documento}")
            else:
                print("No hay documentos en la cola de impresion para imprimir.")
        else:
            cola_impresion.append(accion)
            print(f"Documento '{accion}' agregado a la cola de impresion.")


cola_de_impresion()
# -----------------------------------------------------------------------------------
