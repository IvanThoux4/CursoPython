"""Module providing a function printing python version."""


# /* UNIDAD II:
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, logicos, de comparacion, asignacion, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tu quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los numeros comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni multiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

# -----------------------------------------------------------------------------------
# CONSTANTES PARA LAS OPERACIONES
NUMERO_A = 14
NUMERO_B = 3
numeros = [NUMERO_A, NUMERO_B]
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operadores aritmeticos

# SUMA
SUMA = NUMERO_A + NUMERO_B
print("La suma de", NUMERO_A, "y", NUMERO_B, "es:", SUMA)

# RESTA
RESTA = NUMERO_A - NUMERO_B
print("La resta de", NUMERO_A, "y", NUMERO_B, "es:", RESTA)

# MULTIPLACION
MULTIPLICACION = NUMERO_A * NUMERO_B
print("La multiplicacion de", NUMERO_A, "y", NUMERO_B, "es:", MULTIPLICACION)

# DIVISION
DIVISION = NUMERO_A / NUMERO_B
print("La division de", NUMERO_A, "y", NUMERO_B, "es:", DIVISION)

# DIVISION ENTERA
DIVISION_ENTERA = NUMERO_A // NUMERO_B
print("La division entera de", NUMERO_A, "y", NUMERO_B, "es:", DIVISION_ENTERA)

# MODULO / RESTO
MODULO = NUMERO_A % NUMERO_B
print("El modulo de", NUMERO_A, "y", NUMERO_B, "es:", MODULO)

# POTENCIA
POTENCIA = NUMERO_A ** NUMERO_B
print("La potencia de", NUMERO_A, "elevado a", NUMERO_B, "es:", POTENCIA)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operadores de comparacion

# IGUALDAD
print("La igualdad entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A == NUMERO_B)

# DESIGUALDAD
print("La desigualdad entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A != NUMERO_B)

# MAYOR QUE
print("La comparacion mayor que entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A > NUMERO_B)

# MENOR QUE
print("La comparacion menor que entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A < NUMERO_B)

# MAYOR O IGUAL QUE
print("La comparacion mayor o igual que entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A >= NUMERO_B)

# MENOR O IGUAL QUE
print("La comparacion menor o igual que entre", NUMERO_A, "y",
      NUMERO_B, "es:", NUMERO_A <= NUMERO_B)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operadores logicos

# AND
print("La operacion AND entre", NUMERO_A, "y",
      NUMERO_B, "es:", (NUMERO_A > 10) and (NUMERO_B < 5))
# VERDADERO AND VERDADERO = VERDADERO

# OR
print("La operacion OR entre", NUMERO_A, "y",
      NUMERO_B, "es:", (NUMERO_A > 10) or (NUMERO_B < 5))
# VERDADERO OR FALSO = VERDADERO

# NOT
print("La operacion NOT de", NUMERO_A, "es:", not NUMERO_A > 10)
# NOT VERDADERO = FALSO
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operaciones de asignacion

# ASIGNACION
NUMERO_C = 20

# ASIGNACION CON SUMA
NUMERO_C += 5  # NUMERO_C = NUMERO_C + 5

# ASIGNACION CON RESTA
NUMERO_C -= 3  # NUMERO_C = NUMERO_C - 3

# ASIGNACION CON MULTIPLICACION
NUMERO_C *= 2  # NUMERO_C = NUMERO_C * 2

# ASIGNACION CON DIVISION
NUMERO_C /= 4  # NUMERO_C = NUMERO_C / 4

# ASIGNACION CON DIVISION ENTERA
NUMERO_C //= 2  # NUMERO_C = NUMERO_C // 2

# ASIGNACION CON MODULO
NUMERO_C %= 3  # NUMERO_C = NUMERO_C % 3

# ASIGNACION CON POTENCIA
NUMERO_C **= 2  # NUMERO_C = NUMERO_C ** 2
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operadores de identidad

# IS
print("NUMERO_A is NUMERO_B:", NUMERO_A is NUMERO_B)

# IS NOT
print("NUMERO_A is not NUMERO_B:", NUMERO_A is not NUMERO_B)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Operadores de pertenencia

# IN
print("NUMERO_A in numeros:", NUMERO_A in numeros)

# NOT IN
print("NUMERO_B not in numeros:", NUMERO_B not in numeros)
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Condicionales:
# IF, ELIF, ELSE

EDAD = 20

if EDAD < 13:
    print("Niño")
elif EDAD < 18:
    print("Adolescente")
else:
    print("Adulto")

# CONDICIONAL DE UNA SOLA LINEA
MENSAJE = "Mayor de edad" if EDAD >= 18 else "Menor de edad"
print(MENSAJE)

# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Iterativas:
# FOR CON RANGO
SUMA = 0
for i in range(1, 11):
    if i % 2 == 0:
        SUMA += i
print("Suma de pares:", SUMA)

# WHILE
CONTADOR = 5

while CONTADOR > 0:
    print("Contando hacia atras:", CONTADOR)
    CONTADOR -= 1

# BREAK Y CONTINUE
for i in range(1, 11):
    if i == 5:
        continue  # Salta el 5
    if i == 8:
        break     # Se detiene en el 8
    print(i)

# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Manejo de excepciones:

# Division entre dos numeros con manejo de errores
A = 10
B = 0

try:
    resultado = A / B
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
else:
    print("Resultado:", resultado)
finally:
    print("Operacion finalizada.")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# Match y case:

COMANDO = "salir"

match COMANDO:
    case "iniciar":
        print("Iniciando sistema...")
    case "detener":
        print("Deteniendo sistema...")
    case "salir":
        print("Saliendo...")
    case _:
        print("Comando no reconocido")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA: Numeros comprendidos entre 10 y 55,
# pares, no son ni el 16 ni multiplos de 3.

for i in range(10, 56):
    if i % 2 != 0:
        continue
    elif i % 3 == 0:
        continue
    elif i == 16:
        continue
    else:
        print("El valor de 'i' es: ", i)
# -----------------------------------------------------------------------------------
