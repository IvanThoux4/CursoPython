'''Esta es la unidad 2 del camino a la programacion'''
'''
/* UNIDAD II:
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, logicos, de comparacion, asignacion, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
'''
# CONSTANTES PARA LAS OPERACIONES
NUMERO_A = 14
NUMERO_B = 3
numeros = [NUMERO_A, NUMERO_B]

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

# Operadores de comparacion

# IGUALDAD
NUMERO_A == NUMERO_B # --> False
 
# DESIGUALDAD
NUMERO_A != NUMERO_B # --> True

# MAYOR QUE
NUMERO_A > NUMERO_B # --> True

# MENOR QUE
NUMERO_A < NUMERO_B # --> False

# MAYOR O IGUAL QUE
NUMERO_A >= NUMERO_B # --> True

# MENOR O IGUAL QUE
NUMERO_A <= NUMERO_B # --> False

# Operadores logicos

# AND
(NUMERO_A > 10) and (NUMERO_B < 5) # --> True
# VERDADERO AND VERDADERO = VERDADERO

# OR
(NUMERO_A > 10) or (NUMERO_B > 5) # --> True
# VERDADERO OR FALSO = VERDADERO

# NOT
not (NUMERO_A > 10) # --> False
# NOT VERDADERO = FALSO

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

# Operadores de identidad

# IS
NUMERO_A is NUMERO_B  # --> False

# IS NOT
NUMERO_A is not NUMERO_B  # --> True

# Operadores de pertenencia

# IN
NUMERO_A in numeros  # --> True

# NOT IN
NUMERO_B not in numeros  # --> False




