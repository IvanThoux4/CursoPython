"""Module providing a function printing python version."""

# /*
#  * UNIDAD 3:
#  * - Crea ejemplos de funciones basicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parametros ni retorno, con uno o varios parametros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algun ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer mas o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una funcion que reciba dos parametros de tipo cadena de texto y retorne un numero.
#  * - La funcion imprime todos los numeros del 1 al 100. Teniendo en cuenta que:
#  *   - Si el numero es multiplo de 3, muestra la cadena de texto del primer parametro.
#  *   - Si el numero es multiplo de 5, muestra la cadena de texto del segundo parametro.
#  *   - Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La funcion retorna el numero de veces que se ha impreso el numero en lugar de los textos.
#  *
#  * Presta especial atencion a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el codigo se entienda.
#  */


# -----------------------------------------------------------------------------------
# Funcion sin parametros ni retorno


def funcion_sin_parametros():
    """Funcion sin parametros ni retorno."""
    print("Esta es una funcion sin parametros ni retorno.")


funcion_sin_parametros()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion con un parametro y sin retorno


def funcion_con_un_parametro(mensaje):
    """Funcion con un parametro y sin retorno."""
    print("Mensaje:", mensaje)


funcion_con_un_parametro("Hola, esta es una funcion con un parametro.")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion con varios parametros y con retorno


def funcion_con_varios_parametros(a, b):
    """Funcion con varios parametros y con retorno."""
    resultado = a + b
    return resultado


RESULTADO = funcion_con_varios_parametros(5, 10)
print("El resultado de la suma es:", RESULTADO)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Funcion dentro de otra funcion


def funcion_externa():
    """Funcion externa que contiene una funcion interna."""

    def funcion_interna():
        """Funcion interna."""
        print("Esta es una funcion interna dentro de una funcion externa.")

    funcion_interna()


funcion_externa()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Uso de funciones ya creadas en el lenguaje


TEXTO = "python"
print("Texto en mayusculas:", TEXTO.upper())       # str.upper()
print("Maximo de una lista:", max([1, 9, 3, 7]))    # max()
print("Longitud de la palabra:", len(TEXTO))        # len()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Variables locales y globales
VARIABLE_GLOBAL = "Soy una variable global"


def funcion_con_variable_local():
    """Funcion que utiliza una variable local."""
    variable_local = "Soy una variable local"
    print(variable_local)
    print(VARIABLE_GLOBAL)  # Acceso a la variable global


funcion_con_variable_local()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------

# DIFICULTAD EXTRA: Funcion que imprime numeros del 1 al 100 con condiciones


def imprimir_numeros(texto1, texto2) -> int:
    """Imprime numeros del 1 al 100 con condiciones."""
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador += 1
    return contador


print("Cantidad de numeros impresos: ", imprimir_numeros("Texo1", "Texto2"))
# -----------------------------------------------------------------------------------
