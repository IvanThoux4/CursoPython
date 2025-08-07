"""Module providing a function printing python version."""

# /*
#  * UNIDAD 14:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.
#  * /--------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import unittest
from datetime import date, datetime
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion a probrar


def sumar(a, b):
    """Funcion para sumar dos numeros"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a+b
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------


class TestSuma(unittest.TestCase):
    """Clase para definir diferentes tipos de test a realizar"""

    def test_suma_positivos(self):
        """Test suma de numeros positivos"""
        self.assertEqual(sumar(3, 4), 7)

    def test_suma_negativos(self):
        """Test suma de numeros negativos"""
        self.assertEqual(sumar(-3, -4), -7)

    def test_suma_mixtos(self):
        """Test suma de numeros mixtos"""
        self.assertEqual(sumar(-3, 3), 0)

    def test_suma_decimales(self):
        """Test suma de numeros decimales"""
        self.assertEqual(sumar(1.5, 2.3), 3.8)

    def test_suma_type(self):
        """Test del tipo de datos recibidos por la funcion"""
        with self.assertRaises(ValueError):
            sumar("5", 7)
        with self.assertRaises(ValueError):
            sumar(5, "7")
        with self.assertRaises(ValueError):
            sumar("5", "7")
        with self.assertRaises(ValueError):
            sumar("a", 7)
        with self.assertRaises(ValueError):
            sumar(None, 7)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


class TestDatosCorrectos(unittest.TestCase):
    """Clase para realizar un test de los datos del diccionario"""

    def setUp(self):
        self.persona = {
            "Nombre": "Thoux Ivan Ezequiel",
            "Edad": 26,
            "Nacimiento": datetime.strptime("05-07-99", "%d-%m-%y").date(),
            "Lenguajes": ["Python", "C", "JavaScript"]}

    def test_claves_existentes(self):
        """Testear que existan todas las claves requeridas."""
        self.assertIn("Nombre", self.persona)
        self.assertIn("Edad", self.persona)
        self.assertIn("Nacimiento", self.persona)
        self.assertIn("Lenguajes", self.persona)

    def test_valores_correctos(self):
        """Verifica que los valores del diccionario sean los esperados."""
        self.assertIsInstance(self.persona["Nombre"], str)
        self.assertIsInstance(self.persona["Edad"], int)
        self.assertIsInstance(self.persona["Nacimiento"], date)
        self.assertIsInstance(self.persona["Lenguajes"], list)
# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
# Ejercutar test
if __name__ == '__main__':
    unittest.main()
# -----------------------------------------------------------------------------------
