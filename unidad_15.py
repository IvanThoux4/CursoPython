"""Module providing a function printing python version."""

# /*
#  * UNIDAD 15:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)
#  * /------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
from datetime import datetime
import locale
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# FECHA Y HORA ACTUAL
FECHA_ACTUAL = datetime.now()

# FECHA DE NACIMIENTO
FECHA_NACIMIENTO = datetime(1999, 7, 5, 15, 00, 0)

# CALCULAR LA DIFERENCIA EN AÑOS
ANIOS_TRANSCURRIDOS = FECHA_ACTUAL.year - FECHA_NACIMIENTO.year

# AJUSTAR EL CALCULO SI NO SE CUMPIO AÑOS ESTE AÑO
if (FECHA_ACTUAL.month, FECHA_ACTUAL.day) < (FECHA_NACIMIENTO.month, FECHA_NACIMIENTO.day):
    ANIOS_TRANSCURRIDOS -= 1

# Mostrar resultados:
print(f"Fecha actual: {FECHA_ACTUAL}")
print(f"Fecha de nacimiento: {FECHA_NACIMIENTO}")
print(f"Años transcurridos: {ANIOS_TRANSCURRIDOS}")
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DIFICULTAD EXTRA

# Establecer el locale a español de Argentina
locale.setlocale(locale.LC_TIME, 'es_AR.utf8')

# Fecha de cumpleaños
cumple = datetime(1999, 7, 5, 14, 30, 45)

print("Formatos de fecha y hora:")

print("1. Día, mes y año:", cumple.strftime("%d/%m/%Y"))
print("2. Hora, minuto y segundo:", cumple.strftime("%H:%M:%S"))
print("3. Día del año:", cumple.strftime("Día %j del año"))
print("4. Día de la semana (número):", cumple.strftime("%w"))  # 0=domingo
print("5. Día de la semana (nombre):", cumple.strftime("%A"))
print("6. Nombre del mes:", cumple.strftime("%B"))
print("7. Fecha completa textual:", cumple.strftime("%A %d de %B de %Y"))
print("8. Año en dos dígitos:", cumple.strftime("%y"))
print("9. Fecha y hora en ISO 8601:", cumple.isoformat())
print("10. Mes y año abreviado:", cumple.strftime("%b %Y"))
# -----------------------------------------------------------------------------------
