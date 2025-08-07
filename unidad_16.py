"""Module providing a function printing python version."""

#  /*
#  * UNIDAD 16:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
#  * /----------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import datetime
import asyncio
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# EJECUCION DE MANERA ASINCRONA


async def tarea(nombre, duracion):
    """Prueba de funcion asincrona"""
    print("-----------------------------------")
    print(
        f"Tarea: {nombre}, Duracion: {duracion} segundos.")
    print(f"Tarea: {nombre}. Inicio {datetime.datetime.now()}")
    await asyncio.sleep(duracion)
    print(f"Tarea: {nombre}. Finalizacion: {datetime.datetime.now()}")
    print("-----------------------------------")

asyncio.run(tarea("1", 5))
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA


async def tareas_asincronas():
    """Tareas asincronas desafio extra"""
    await asyncio.gather(tarea("C", 3), tarea("B", 2), tarea("A", 1))
    await tarea("D", 1)

asyncio.run(tareas_asincronas())
# -----------------------------------------------------------------------------------
