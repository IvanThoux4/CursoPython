"""Module providing a function printing python version."""

# /*
#  * UNIDAD 32: SIMULADOR JUEGOS OLIMPICOS
#  * ¡Los JJOO de París 2024 han comenzado!
#  * Crea un programa que simule la celebración de los juegos.
#  * El programa debe permitir al usuario registrar eventos y participantes,
#  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
#  * y generar un informe final. Todo ello por terminal.
#  * Requisitos:
#  * 1. Registrar eventos deportivos.
#  * 2. Registrar participantes por nombre y país.
#  * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
#  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
#  * 5. Mostrar los ganadores por cada evento.
#  * 6. Mostrar el ranking de países según el número de medallas.
#  * Acciones:
#  * 1. Registro de eventos.
#  * 2. Registro de participantes.
#  * 3. Simulación de eventos.
#  * 4. Creación de informes.
#  * 5. Salir del programa.
#  * /---------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
import random
# 1) Evento


class Evento:
    """Clase: evento"""

    def __init__(self, nombre_evento):
        self.nombre = nombre_evento
        self.participantes = []

    def agregar_participante(self, participante):
        """Funcion: agregar participante"""
        self.participantes.append(participante)

    def __str__(self):
        return f"Evento: {self.nombre} ({len(self.participantes)}) participantes"


# 2) Participante
class Participante:
    """Clase: participante"""

    def __init__(self, nombre_completo, pais):
        self.nombre = nombre_completo
        self.pais = pais

    def __str__(self):
        return f"{self.nombre}: ({self.pais})"

# 3) Medallero


class Medallero:
    """Clase: medallero"""

    def __init__(self):
        self.paises = {}  # {pais: {"oro" : 0, "plata" : 0, "bronce" : 0}}

    def agregar_medalla(self, pais, tipo):
        """Funcion: agregar medalla"""
        if pais not in self.paises:
            self.paises[pais] = {"oro": 0, "plata": 0, "bronce": 0}
        self.paises[pais][tipo] += 1

    def ranking(self):
        """Funcion: ranking"""
        return sorted(
            self.paises.items(),
            key=lambda x: (x[1]["oro"], x[1]["plata"], x[1]["bronce"]),
            reverse=True
        )

# 4) Simulador de eventos


class SimuladorEventos:
    """Clase: simulador de eventos"""

    def simular(self, evento):
        """Funcion: simular"""
        if len(evento.participantes) < 3:
            return None

        participantes = evento.participantes[:]
        random.shuffle(participantes)

        return {
            "oro": participantes[0],
            "plata": participantes[1],
            "bronce": participantes[2]
        }

# 5) Juegos olimpicos


class JuegosOlimpicos:
    """Clase: juegos olimpicos"""

    def __init__(self):
        self.eventos = []
        self.resultados = {}
        self.medallero = Medallero()
        self.simulador = SimuladorEventos()

    def registrar_evento(self, nombre):
        """Funcion: registrar evento"""
        self.eventos.append(Evento(nombre))

    def registrar_participante(self, nombre_completo, pais, evento_nombre):
        """Funcion: registrar participante"""
        evento = next(
            (e for e in self.eventos if e.nombre == evento_nombre), None)
        if evento:
            evento.agregar_participante(Participante(nombre_completo, pais))

    def simular_eventos(self):
        """Funcion: simular eventos"""
        for evento in self.eventos:
            resultado = self.simulador.simular(evento)
            if resultado:
                self.resultados[evento.nombre] = resultado
                for tipo, participante in resultado.items():
                    self.medallero.agregar_medalla(participante.pais, tipo)

    def mostrar_resultados(self):
        """Funcion: mostrar resultados"""
        for evento, podio in self.resultados.items():
            print(f"\n{evento}:")
            for tipo, participante in podio.items():
                print(f" {tipo.capitalize()}: {participante}")

    def mostrar_ranking(self):
        """Funcion: mostrar ranking"""
        print("\n---- Ranking de paises ----")
        for pais, medallas in self.medallero.ranking():
            print(f"----- {pais} -----")
            print(f"- Oro: {medallas['oro']}")
            print(f"- Plata: {medallas['plata']}")
            print(f"- Bronce: {medallas['bronce']}")

# 6) Menu de interaccion


def menu():
    """Funcion: menu"""
    jjoo = JuegosOlimpicos()

    while True:
        print("\n---- Menú Juegos Olímpicos ----")
        print("1. Registrar evento")
        print("2. Registrar participante")
        print("3. Simular eventos")
        print("4. Mostrar informe")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            nombre_evento = input("Nombre del evento: ")
            jjoo.registrar_evento(nombre_evento)
        elif opcion == "2":
            if not jjoo.eventos:
                print("Se debe registrar un evento primero.")
                continue
            nombre_completo = input("Ingrese nombre del participante: ")
            pais = input("Ingrese nombre del pais: ")
            print("Eventos disponibles: ", [e.nombre for e in jjoo.eventos])
            evento_nombre = input("Ingrese nombre del evento: ")
            jjoo.registrar_participante(nombre_completo, pais, evento_nombre)
        elif opcion == "3":
            jjoo.simular_eventos()
            print("Simulacion completada.")
        elif opcion == "4":
            jjoo.mostrar_resultados()
            jjoo.mostrar_ranking()
        elif opcion == "5":
            print("Usted salio del menu.")
            break
        else:
            print("Opcion no valida.")


# 7) main para realizar pruebas
if __name__ == "__main__":
    menu()
# -------------------------------------------------------------------------------------
