"""Module providing a function printing python version."""

# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  *
#  * UNIDAD 13:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borra los archivos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.
#  * /----------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import xml.dom.minidom
import xml.etree.ElementTree as ET  # Librería para trabajar con XML
import json  # Librería para trabajar con JSON
import os  # Librería para trabajar con el sistema de archivos
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Datos de ejemplo

datos = {
    "Nombre": "Ivan Ezequiel Thoux",
    "Edad": 26,
    "Fecha_de_nacimiento": "1999-07-05",
    "Lenguajes_de_programacion": ["Python", "JavaScript", "C++"]
}
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Crear archivo JSON
with open("datos.json", "w", encoding="utf-8") as json_file:
    json.dump(datos, json_file, indent=4, ensure_ascii=False)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Crear archivo XML

persona = ET.Element("persona")

ET.SubElement(persona, "Nombre").text = datos["Nombre"]
ET.SubElement(persona, "Edad").text = str(datos["Edad"])
ET.SubElement(
    persona, "Fecha_de_nacimiento").text = datos["Fecha_de_nacimiento"]

lenguajes_1 = ET.SubElement(persona, "lenguajes_programacion")
for lenguaje_1 in datos["Lenguajes_de_programacion"]:
    ET.SubElement(lenguajes_1, "Lenguaje").text = lenguaje_1

# Escribir XML en archivo
arbol = ET.ElementTree(persona)
arbol.write("datos.xml", encoding="utf-8", xml_declaration=True)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Mostrar contenido JSON

print("\nContenido de datos.json: ")
with open("datos.json", "r", encoding="utf-8") as json_file:
    print(json_file.read())
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Mostrar contenido XML
print("\nContenido de datos.xml: ")
with open("datos.xml", "r", encoding="utf-8") as archivo_xml:
    xml_str = archivo_xml.read()
    dom = xml.dom.minidom.parseString(xml_str)
    print(dom.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8"))
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Eliminar archivos

os.remove("datos.json")
os.remove("datos.xml")
print("\nArchivos eliminados correctamente.")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA

# Crear clase


class Persona:
    """Definicion de la clase persona"""

    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        """Funcion para inicializar los parametros de una persona"""
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    def mostrar(self):
        """Funcion para mostrar los datos de una persona registrada"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        for lenguaje_f in self.lenguajes:
            print(f"- {lenguaje_f}")

    def to_dict(self):
        """Devuelve los datos de la persona como un diccionario"""
        return {
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Fecha_de_nacimiento": self.fecha_nacimiento,
            "Lenguajes_programacion": self.lenguajes
        }

# Crear archivos con datos de prueba


datos = {
    "Nombre": "Ivan Ezequiel Thoux",
    "Edad": 26,
    "Fecha_de_nacimiento": "1999-07-05",
    "Lenguajes_programacion": ["Python", "C", "JavaScript"]
}

# JSON

with open("archivo.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)

# XML
persona_xml = ET.Element("persona")
ET.SubElement(persona_xml, "Nombre").text = datos["Nombre"]
ET.SubElement(persona_xml, "Edad").text = str(datos["Edad"])
ET.SubElement(
    persona_xml, "Fecha_de_nacimiento").text = datos["Fecha_de_nacimiento"]

lenguajes_xml = ET.SubElement(persona_xml, "Lenguajes_programacion")
for lenguaje in datos["Lenguajes_programacion"]:
    ET.SubElement(lenguajes_xml, "Lenguaje").text = lenguaje

ET.ElementTree(persona_xml).write(
    "archivo.xml", encoding="utf-8", xml_declaration=True)

# Leer desde JSON y crear una instancia

with open("archivo.json", "r", encoding="utf-8") as f:
    datos_json = json.load(f)
    persona_json = Persona(
        datos_json["Nombre"],
        datos_json["Edad"],
        datos_json["Fecha_de_nacimiento"],
        datos_json["Lenguajes_programacion"]
    )

# Leer desde XML y crear una instancia

arbol = ET.parse("archivo.xml")
raiz = arbol.getroot()

nombre_xml = raiz.find("Nombre").text
edad_xml = int(raiz.find("Edad").text)
fecha_nacimiento_xml = raiz.find("Fecha_de_nacimiento").text
lenguajes_xml = [elem.text for elem in raiz.find(
    "Lenguajes_programacion").findall("Lenguaje")]

# Mostrar resultados

print("\nDatos desde JSON: ")
persona_json.mostrar()

print("\nDatos desde XML: ")
persona_desde_xml = Persona(
    nombre_xml,
    edad_xml,
    fecha_nacimiento_xml,
    lenguajes_xml
)
persona_desde_xml.mostrar()

# Borrar archivos
os.remove("archivo.json")
os.remove("archivo.xml")
print("\nArchivos eliminados correctamente.")
