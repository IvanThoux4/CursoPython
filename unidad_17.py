"""Module providing a function printing python version."""

# /*
#  * UNIDAD 17: EXPRESIONES REGULARES
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  * /-----------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import re
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Las expresiones regulares son una herramienta poderosa para buscar patrones dentro
# de un texto. En python se utilizan mediante el modulo "import re".
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# EXPRESIONES REGULARES


def encontrar_numeros(texto):
    """Funcion para encontrar la cantidad de numeros en un texto"""
    # Encuentra numeros entero y decimales
    return re.findall(r"\d+(?:\.\d+)?", texto)

# '\d+' Uno o mas digitos (numeros enteros)
# '(?: ....)' Grupo no capturador (no se crea una sublista)
# '\.' Un punto literal (para los decimales)
# '\d+' Uno o mas digitos (ahora para la parte decimal)
# '?' El grupo decimal es opcional


numeros = encontrar_numeros(
    "Tengo 2 perros, 1.5 litros de agua, 300 amigos y 0.75 bitcoins.")
print(f"Numeros encontrados: {numeros}")
# Los numeros encontrados deberian ser: ['2', '1.5', '300', '0.75']
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA

# Validar un e-mail


def validar_email(email):
    """Funcion para validar que sea un e-mail"""
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

# '^' indica el inicio de la cadena
# '[\w.+-]' busca caracteres que pueden ser letras, numeros, guiones, puntos y simbolos
# '@' es el simbolo que separa el usuario del dominio del email
# '[\w]+' busca uno o mas caracteres para el nobmre del dominio
# '\.' representa el punto que separa el dominio de la extension
# '[a-zA-Z]+' busca una o mas letras para la extension del dominio (com, net, org)
# '$' indica el final de la cadena


CORREO_A = 'thouxivan@gmail.com'
CORREO_B = 'thouxivan.hotmail.net'
print(f"Es un mail valido: {validar_email(CORREO_A)}")
print(f"Es un mail valido: {validar_email(CORREO_B)}")

# Validar numero de telefono


def validar_telefono(telefono):
    """Funcion para validar que sea un numero telefonico"""
    return bool(re.match(r"^\+?\d{1,4}[\s-]?\d{2,4}[\s-]?\d{4,6}$", telefono))

# '^' indica el inicio de la cadena
# '\+?' permite que opcionalmente aparezca el simbolo +
# '\d{1,4}' busca entre 1 y 4 digitos que corresponden al codigo del pais
# '[\s-]?' permite opcionalmente un espacio o guion como separador
# '\d{2, 4}' busca entre 2 y 4 digitos, para el codigo de area
# '[\s-]?' permite opcionalmente un espacio o guion como separador
# '\d{4, 8}' busca entre 4 y 8 digitos que suelen ser para el numero local
# '$' indica el final de la cadena


NUMERO_A = '+54 3758-484598'
NUMERO_B = '+54 ABCD-484598'
print(f"Es un telefono valido: {validar_telefono(NUMERO_A)}")
print(f"Es un telefono valido: {validar_telefono(NUMERO_B)}")

# Validar una URL


def validar_url(url):
    """Funcion para validar que sea una URL"""
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

# '^' indica el inicio de la cadena
# 'http[s]?://' busca la secuencia http:// o https://
# '(www.)?' permite opcionalmente el prefijo www.
# '[\w]' busca uno o mas caracteres alfanumericos o guiones bajos para el nobmre del dominio
# '\.' representa el punto que separa el dominio de la extension
# '[a-zA-Z]{2,}' busca una extensión de dominio compuesta por al menos dos letras (com, org)
# '$' indica el final de la cadena


URL_A = 'https://www.moure.dev'
URL_B = 'hattpr://ww3w.cuevana3.org'
print(f"Es un url valido: {validar_url(URL_A)}")
print(f"Es un url valido: {validar_url(URL_B)}")
# -----------------------------------------------------------------------------------
