"""Module providing a function printing python version."""

# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  * /-------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
import os  # librería para manejar archivos y directorios
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Datos personales
USUARIO_GITHUB = "IvanThoux"
NOMBRE = "Iván Thoux"
EDAD = 26
LENGUAJE_FAVORITO = "Python"
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Crear archivo con el nombre de usuario de GitHub
ARCHIVO = f"{USUARIO_GITHUB}.txt"
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Crear y escribir en el archivo
with open(ARCHIVO, 'w', encoding='utf-8') as f:
    f.write(f"Nombre: {NOMBRE}\n")
    f.write(f"Edad: {EDAD}\n")
    f.write(f"Lenguaje favorito: {LENGUAJE_FAVORITO}\n")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Leer y mostrar el contenido del archivo
print("Contenido del archivo:")
with open(ARCHIVO, 'r', encoding='utf-8') as f:
    print(f.read())
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Borrar el archivo
os.remove(ARCHIVO)
print(f"Archivo {ARCHIVO} eliminado correctamente.")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA:

ARCHIVO_VENTAS = "ventas.txt"


def agregar_producto():
    """Funcion para añadir un producto a una lista de ventas"""
    nombre = input("Nombre del producto: ").strip()
    cantidad = input("Cantidad vendida: ").strip()
    precio = input("Precio unitario: ").strip()
    with open(ARCHIVO_VENTAS, "a", encoding="utf-8") as fi:
        fi.write(f"{nombre},{cantidad},{precio}\n")
    print("Producto agregado exitosamente.\n")


def consultar_productos():
    """Funcion para consultar los productos registrados"""
    if not os.path.exists(ARCHIVO_VENTAS):
        print("No hay productos cargados.\n")
        return
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as fi:
        print("Productos registrados: ")
        for linea in fi:
            nombre, cantidad, precio = linea.strip().split(",")
            print(f"- {nombre}: {cantidad} de unidades, ${precio} c/u.")
        print()


def actualizar_producto():
    """Funcion para actualizar un producto si se encuentra dentro del archivo"""
    nombre_actualizar = input("Nombre del producto a actualizar: ").strip()
    encontrado = False
    nuevos_datos = []
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as fi:
        for linea in fi:
            nombre, _, _ = linea.strip().split(",")
            if nombre == nombre_actualizar:
                nueva_cantidad = input("Nueva cantidad vendida: ").strip()
                nuevo_precio = input("Nuevo precio: ").strip()
                nuevos_datos.append(
                    f"{nombre},{nueva_cantidad},{nuevo_precio}\n")
                encontrado = True
            else:
                nuevos_datos.append(linea)
    if encontrado:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as fi:
            fi.writlines(nuevos_datos)
        print("Producto actualizado exitosamente.\n")
    else:
        print("Producto no encontrado.\n")


def eliminar_producto():
    """Funcion para eliminar un producto que se encuentre dentro del registro"""
    nombre_eliminar = input("Nombre del producto a eliminar: ").strip()
    encontrado = False
    nuevos_datos = []
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as fi:
        for linea in fi:
            nombre, _, _ = linea.strip().split(",")
            if nombre == nombre_eliminar:
                encontrado = True
            else:
                nuevos_datos.append(linea)
    if encontrado:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as fi:
            fi.writelines(nuevos_datos)
        print("Producto eliminado exitosamente.\n")
    else:
        print("Producto no encontrado.\n")


def venta_total():
    """Funcion para calcular el total de una venta"""
    total = 0
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as fi:
        for linea in fi:
            _, cantidad, precio = linea.strip().split(",")
            total += int(cantidad) * float(precio)
    print(f"Venta total: ${total:.2f}.\n")


def venta_por_producto():
    """Funcion para calcular el total de ventas de un producto"""
    nombre_buscar = input("Nombre del producto: ").strip()
    encontrado = False
    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as fi:
        for linea in fi:
            nombre, cantidad, precio = linea.strip().split(",")
        if nombre == nombre_buscar:
            total = int(cantidad) * float(precio)
            print(
                f"Venta de {nombre}: {cantidad} * ${precio} = ${total:.2f}.\n")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.\n")


def menu():
    """Funcion para desplegar el menu de opciones"""
    while True:
        print("===== GESTIÓN DE VENTAS =====")
        print("1. Añadir producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir y borrar archivo")
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            venta_total()
        elif opcion == "6":
            venta_por_producto()
        elif opcion == "7":
            if os.path.exists(ARCHIVO_VENTAS):
                os.remove(ARCHIVO_VENTAS)
            print("Archivo borrado y programa finalizado.")
            break
        else:
            print("Opción no válida.\n")


# Ejecutar el menu
menu()
# -----------------------------------------------------------------------------------
