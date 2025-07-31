"""Module providing a function printing python version."""

# /*
#  * UNIDAD 4:
#  * - Muestra ejemplos de creacion de todas las estructuras soportadas por defecto
#  *   en tu lenguaje.
#  * - Utiliza operaciones de insercion, borrado, actualizacion y ordenacion.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de busqueda, insercion, actualizacion
#  *   y eliminacion de contactos.
#  * - Cada contacto debe tener un nombre y un numero de telefono.
#  * - El programa solicita en primer lugar cuál es la operacion que se quiere realizar,
#  *   y a continuacion los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir numeros de telefono no numericos y con más
#  *   de 11 digitos (o el numero de digitos que quieras).
#  * - Tambien se debe proponer una operacion de finalizacion del programa.
# * /------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
# LISTAS

# CREACION
frutas = ["manzana", "banana", "naranja"]
print("Lista de frutas:", frutas)

# INSERCION
frutas.append("kiwi")  # Añadir kiwi al final de la lista
frutas.insert(1, "fresa")  # Insertar fresa en la segunda posicion
print("Lista de frutas tras inserciones:", frutas)

# ACTUALIZACION DE ELEMENTOS
frutas[0] = "manzana verde"  # Cambiar manzana por manzana verde

# ELIMINACION
frutas.remove("naranja")  # Eliminar por valor de la lista
eliminado = frutas.pop()  # Eliminar el ultimo elemento y guardarlo en una variable
del frutas[1]  # Eliminar el elemento en la segunda posicion
print("Lista de frutas tras actualizaciones y eliminaciones:", frutas)

# ORDENACION
frutas.sort()  # Ordenar la lista alfabeticamente
print("Lista de frutas ordenada:", frutas)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# TUPLAS

# CREACION
colores = ("rojo", "verde", "azul")
print("Tupla de colores:", colores)
# Las tuplas son inmutables, no se pueden modificar directamente
# Sin embargo, se puede crear una nueva tupla a partir de la existente
# Añadir amarillo creando una nueva tupla
colores_nuevos = colores + ("amarillo",)
print("Tupla de colores tras creacion de nueva tupla:", colores_nuevos)

# Ademas se pueden transformar a listas para modificarlas
colores_lista = list(colores)  # Convertir tupla a lista
colores_lista.append("morado")
colores = tuple(colores_lista)  # Convertir de nuevo a tupla
print("Tupla de colores tras conversion a lista y modificacion:", colores)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DICCIONARIOS

# CREACION
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario de persona:", persona)

# INSERCION
persona["telefono"] = "123456789"  # Añadir un nuevo par clave-valor
print("Diccionario de persona tras insercion:", persona)

# ACTUALIZACION
persona["edad"] = 31  # Actualizar el valor de la clave 'edad'
print("Diccionario de persona tras actualizacion:", persona)

# ELIMINACION
del persona["ciudad"]  # Eliminar la clave 'ciudad'
print("Diccionario de persona tras eliminacion:", persona)
persona.pop("telefono")  # Eliminar y retornar el valor de 'telefono'
print("Diccionario de persona tras pop:", persona)

# ORDENACION: Los diccionarios no mantienen un orden especifico,
# pero se pueden ordenar por claves o valores al convertirlos a una lista.
print("Ordenado por clave: ", dict(sorted(persona.items())))
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONJUNTOS

# CREACION
numeros = {1, 2, 3, 4}
print("Set de numeros:", numeros)

# INSERCION
numeros.add(5)  # Añadir un nuevo elemento
print("Set de numeros tras insercion:", numeros)

# ACTUALIZACION: Los conjuntos no tienen actualizacion directa,
# pero se pueden añadir nuevos elementos.
numeros.update([6, 7])  # Añadir varios elementos
print("Set de numeros tras actualizacion:", numeros)

# ELIMINACION
numeros.remove(2)  # Eliminar un elemento especifico
print("Set de numeros tras eliminacion:", numeros)

# ORDENACION: Los conjuntos no tienen un orden especifico, pero se pueden convertir a una lista.
numeros_ordenados = sorted(numeros)  # Ordenar el conjunto
print("Set de numeros ordenado:", numeros_ordenados)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# FROZEN SETS: conjuntos inmutables
# Utiles para crear claves en diccionarios o elementos en conjuntos.

# CREACION
numeros_frozen = frozenset([1, 2, 3, 4])
print("Frozen set de numeros:", numeros_frozen)
# No se pueden modificar, insertar valores o eliminar elementos de un frozen set.
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CADENAS

# CREACION
TEXTO = "python"
print("Cadena de texto:", TEXTO)

# INSERCION: Las cadenas son inmutables, no se pueden modificar directamente.
# Sin embargo, se puede crear una nueva cadena a partir de la existente.
TEXTO_NUEVO = TEXTO + " es genial"
print("Cadena de texto tras insercion:", TEXTO_NUEVO)

# ACTUALIZACION: Similar a la insercion, se crea una nueva cadena.
TEXTO_ACTUALIZADO = TEXTO_NUEVO.replace("genial", "increible")
print("Cadena de texto tras actualizacion:", TEXTO_ACTUALIZADO)

# ELIMINACION: No se pueden eliminar caracteres de una cadena directamente,
# pero se puede crear una nueva cadena sin el carácter a eliminar.
TEXTO_ELIMINADO = TEXTO_ACTUALIZADO.replace("python", "")
# Eliminar espacios al inicio y final
print("Cadena de texto tras eliminacion:", TEXTO_ELIMINADO.strip())

# ORDENACION: Las cadenas se pueden ordenar alfabeticamente convirtiendolas en una lista.
TEXTO_ORDENADO = sorted(TEXTO_ACTUALIZADO)
print("Cadena de texto ordenada:", TEXTO_ORDENADO)
# Convertir lista de caracteres a cadena
TEXTO_ORDENADO = ''.join(TEXTO_ORDENADO)
print("Cadena de texto ordenada como string:", TEXTO_ORDENADO)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# FUNCION EXTRA: Agenda de contactos


def agenda_contactos():
    """Funcion para gestionar una agenda de contactos."""
    agenda = {}

    def insertar_contacto(nombre):
        """Insertar un nuevo contacto en la agenda."""
        telefono = input("Introduce el numero de telefono (max 11 digitos): ")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[nombre] = telefono
        else:
            print(
                "Numero de telefono no valido. Debe ser numerico y tener maximo 11 digitos.")

    while True:
        print("\n---------------------------")
        print("Agenda de Contactos")
        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar contactos")
        print("6. Salir")
        print("---------------------------")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                nombre = input("Introduce el nombre del contacto: ")
                insertar_contacto(nombre)
            case "2":
                nombre = input("Introduce el nombre del contacto a buscar: ")
                if nombre in agenda:
                    print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
                else:
                    print(f"Contacto {nombre} no encontrado.")
            case "3":
                nombre = input(
                    "Introduce el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    insertar_contacto(nombre)
                else:
                    print(f"Contacto {nombre} no encontrado.")
            case "4":
                nombre = input("Introduce el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                else:
                    print(f"Contacto {nombre} no encontrado.")
            case "5":
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            case "6":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opcion no valida. Intente de nuevo.")


agenda_contactos()
