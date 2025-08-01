"""Module providing a function printing python version."""

# /*
#  * UNIDAD 5:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrian ser (busca todas las que puedas):
#  * - Acceso a caracteres especificos, subcadenas, longitud, concatenacion, repeticion,
#  *   recorrido, conversion a mayusculas y minusculas, reemplazo, division, union,
#  *   interpolacion, verificacion...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palindromos
#  * - Anagramas
#  * - Isogramas
#  * /---------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CADENA BASE

CADENA = "Python es un lenguaje de programacion versatil y poderoso."
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# ACCESO A CARACTERES Y SUBCADENAS

PRIMER_CARACTER = CADENA[0]  # Acceso al primer caracter
print("Primer caracter:", PRIMER_CARACTER)

ULTIMO_CARACTER = CADENA[-1]  # Acceso al ultimo caracter
print("Ultimo caracter:", ULTIMO_CARACTER)

# Subcadena desde el indice 0 al 5
print("Subcadena (del 0 al 5):", CADENA[:5])
print("Subcadena (del 7 al final):", CADENA[7:])
print("Reversa de la cadena:", CADENA[::-1])
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# LONGITUD DE LA CADENA

LONGITUD = len(CADENA)  # Longitud de la cadena
print("Longitud de la cadena:", LONGITUD)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONCATENACION Y REPETICION

SALUDO = "Hola"
NOMBRE = "Ivan"
FRASE = SALUDO + ", " + NOMBRE + "!"  # Concatenacion de cadenas
print("Frase concatenada:", FRASE)

ECO = "Eco! " * 3  # Repeticion de cadena
print("Eco repetido:", ECO)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONVERSION A MAYUSCULAS Y MINUSCULAS

MAYUSCULAS = CADENA.upper()  # Convertir a mayusculas
print("Cadena en mayusculas:", MAYUSCULAS)

MINUSCULAS = CADENA.lower()  # Convertir a minusculas
print("Cadena en minusculas:", MINUSCULAS)

CAPITALIZADA = CADENA.capitalize()  # Capitalizar la cadena
print("Cadena capitalizada:", CAPITALIZADA)

TITULO = CADENA.title()  # Convertir a titulo
print("Cadena en formato titulo:", TITULO)

INVERTIDA = CADENA.swapcase()  # Intercambiar mayusculas y minusculas
print("Cadena con mayusculas y minusculas invertidas:", INVERTIDA)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# REEMPLAZO Y DIVISION
TEXTO_ACTUALIZADO = CADENA.replace("Python", "Java")  # Reemplazar texto
print("Cadena tras reemplazo:", TEXTO_ACTUALIZADO)

# Dividir la cadena en palabras
PALABRAS = CADENA.split()  # Dividir por espacios
print("Palabras en la cadena:", PALABRAS)

# Dividir la cadena por un caracter especifico
PALABRAS_COMA = CADENA.split(" ")  # Dividir por espacios
print("Palabras divididas por espacio:", PALABRAS_COMA)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# UNION

PALABRAS = ["Python", "es", "genial"]
UNION = " ".join(PALABRAS)  # Unir palabras con un espacio
print("Palabras unidas:", UNION)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# VERIFICACION DE CONTENIDO

# Verificar si contiene una subcadena
CONTIENE_PYTHON = "Python" in CADENA
print("¿Contiene 'Python'?:", CONTIENE_PYTHON)

# Verificar si es un palindromo
ES_PALINDROMO = CADENA == CADENA[::-1]
print("¿Es un palindromo?:", ES_PALINDROMO)

# Verificar si una cadena es un isograma (sin letras repetidas)
ES_ISOGRAMA = len(CADENA) == len(set(CADENA.replace(" ", "").lower()))
print("¿Es un isograma?:", ES_ISOGRAMA)

# Verificar si empieza con una subcadena
EMPIEZA_CON = CADENA.startswith("Python")
print("¿Empieza con 'Python'?:", EMPIEZA_CON)

# Verificar si termina con una subcadena
TERMINA_CON = CADENA.endswith("poderoso.")
print("¿Termina con 'poderoso.'?:", TERMINA_CON)

# Verificar si esta vacio
ESTA_VACIO = not CADENA.strip()  # Verificar si la cadena esta vacia
print("¿La cadena esta vacia?:", ESTA_VACIO)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# BUSQUEDA

# Buscar la posicion de una subcadena
POSICION = CADENA.find("lenguaje")
print("Posicion de 'lenguaje':", POSICION)

# Buscar el indice de una subcadena devuelve un error si no se encuentra
INDICE = CADENA.index("o")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# CONTEO DE CARACTERES

CONTEO = CADENA.count("o")  # Contar ocurrencias de una subcadena
print("Conteo de 'o':", CONTEO)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# ELIMINACION DE ESPACIOS

CADENA_CON_ESPACIOS = "   Python es genial   "
print("Cadena con espacios:", CADENA_CON_ESPACIOS)

# Eliminar espacios al inicio y final
CADENA_SIN_ESPACIOS = CADENA_CON_ESPACIOS.strip()
print("Cadena sin espacios:", CADENA_SIN_ESPACIOS)

# Eliminar espacios al inicio
CADENA_SIN_ESPACIOS_INICIO = CADENA_CON_ESPACIOS.lstrip()
print("Cadena sin espacios al inicio:", CADENA_SIN_ESPACIOS_INICIO)

# Eliminar espacios al final
CADENA_SIN_ESPACIOS_FINAL = CADENA_CON_ESPACIOS.rstrip()
print("Cadena sin espacios al final:", CADENA_SIN_ESPACIOS_FINAL)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# INTERPOLACION / FORMATEO DE CADENAS

NOMBRE = "Ivan"
EDAD = 26

# Formateo con f-strings (Python 3.6+)
FORMATEO_FSTRING = f"Hola, mi nombre es {NOMBRE} y tengo {EDAD} años."
print("Formateo con f-strings:", FORMATEO_FSTRING)

# Formateo con format()
FORMATEO_FORMAT = "Hola, mi nombre es {} y tengo {} años.".format(NOMBRE, EDAD)
print("Formateo con format():", FORMATEO_FORMAT)

# Formateo con % (antiguo estilo)
FORMATEO_PERC = "Hola, mi nombre es %s y tengo %d años." % (NOMBRE, EDAD)
print("Formateo con %:", FORMATEO_PERC)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# VERIFICACION DE PROPIEDADES

TEXTO_1 = "Python"
TEXTO_2 = "12345"
TEXTO_3 = "Python3"

# Verificar si es alfanumerico
print("¿'Python' es alfanumerico?:", TEXTO_3.isalnum())

# Verificar si es alfabetico
print("¿'Python' es alfabetico?:", TEXTO_1.isalpha())

# Verificar si es numerico
print("¿'12345' es numerico?:", TEXTO_2.isdigit())
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# FUNCION EXTRA: Crea un programa que analice dos palabras diferentes y realice
# comprobaciones para descubrir si son palindromos, anagramas e isogramas.


def analizar_palabras(palabra1, palabra2):
    """Analiza dos palabras y verifica si son palindromos, anagramas e isogramas."""

    # Analizar si las palabras son palindromos
    print(f"¿Es {palabra1} un palindromo?: {palabra1 == palabra1[::-1]}")
    print(f"¿Es {palabra2} un palindromo?: {palabra2 == palabra2[::-1]}")

    # Analizar si las palabras son anagramas
    print(
        f"¿Es {palabra1} anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}")

    def es_isograma(palabra):

        palabra_diccionario = dict()
        for caracter in palabra:
            palabra_diccionario[caracter] = palabra_diccionario.get(
                caracter, 0) + 1

        isograma = True
        valores = list(palabra_diccionario.values())
        longitud_isograma = valores[0]
        for contar_palabra in valores:
            if contar_palabra != longitud_isograma:
                isograma = False
                break

        return isograma

    print(f"¿{palabra1} es un isograma?: {es_isograma(palabra1)}")
    print(f"¿{palabra2} es un isograma?: {es_isograma(palabra2)}")


analizar_palabras("reconocer", "correr")  # Ejemplo de palabras
analizar_palabras("amor", "roma")  # Otro ejemplo de palabras
# -----------------------------------------------------------------------------------
