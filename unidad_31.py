"""Module providing a function printing python version."""

# /*
#  * UNIDAD 31: SOLID: PRINCIPIO DE INVERSION DE DEPENDENCIAS (DIP)
#  * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
#  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un sistema de notificaciones.
#  * Requisitos:
#  * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
#  * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
#  * Instrucciones:
#  * 1. Crea la interfaz o clase abstracta.
#  * 2. Desarrolla las implementaciones específicas.
#  * 3. Crea el sistema de notificaciones usando el DIP.
#  * 4. Desarrolla un código que compruebe que se cumple el principio.
#  * /--------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Los modulos de alto nivel no deben depender de modulos de bajo nivel. Ambos deben
# depender de abstracciones. Las abstracciones no deben depender de detalles; los
# detalles deben depender de abstracciones. En otras palabras, el codigo que coordina
# la logica principal (alto nivel) no debe conocer implementaciones concretas, solo
# interfaces o clases abstractas. Esto permite cambiar las implementaciones sin
# modificar el codigo principal
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Ejemplo incorrecto (violando DIP)
# En este ejemplo, una clase Notificador (alto nivel) depende directamente de clases
# concretas de envio de mensajes (bajo nivel)

# Modulo de alto nivel


from typing import List
from abc import ABC, abstractmethod


class Notificador:
    """Clase notificador"""

    def __init__(self):
        # Dependencia directa de una clase concreta
        self.email_sender = EmailSender()

    def enviar(self, mensaje):
        """Funcion: enviar mensaje"""
        self.email_sender.enviar_email(mensaje)

# Modulo de bajo nivel


class EmailSender:
    """Clase enviar email"""

    def enviar_email(self, mensaje):
        """Funcion: enviar email"""
        print(f"Enviando email: {mensaje}...")


# Uso
notificador = Notificador()
notificador.enviar("Hola usuario!")
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Ejemplo correcto (cumpliendo DIP)

# Abstraccion


class CanalNotificacion(ABC):
    """Clase: canal de notificaciones"""
    @abstractmethod
    def enviar(self, mensaje):
        """Funcion: enviar mensaje"""

# Implementaciones concretas (bajo nivel)


class EnviarEmail(CanalNotificacion):
    """Clase: enviar email"""

    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}...")


class EnviarSMS(CanalNotificacion):
    """Clase: enviar SMS"""

    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}...")

# Modulo de alto nivel (solo conoce la abstraccion)


class Notificathor:
    """Clase: notificador"""

    def __init__(self, canal: CanalNotificacion):
        self.canal = canal

    def enviar(self, mensaje):
        """Funcion: enviar mensaje"""
        self.canal.enviar(mensaje)


# Podemos cambiar la implementacion sin tocar Notificador
email_sender = EnviarEmail()
sms_sender = EnviarSMS()

notificador_email = Notificathor(email_sender)
notificador_email.enviar("Hola por E-mail!")

notificador_sms = Notificathor(sms_sender)
notificador_sms.enviar("Hola por SMS!")

# Notificathor no sabe como se envia el mensaje. Cambiar de email o SMS o WhatsApp no
# implica modificar Notificathor. Facilita las pruebas unitarias, ya que podemos
# inyectar mocks o fakes
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

# 1) Abstraccion (Interfaz)


class CanalNotificaciones(ABC):
    """Canal de notificaciones"""
    @abstractmethod
    def enviar(self, destino, mensaje):
        """Envia un mensaje al destino especificado"""
        raise NotImplementedError


# 2) Implementaciones concretas (bajo nivel)
class EnviadorEmail(CanalNotificaciones):
    """Clase: enviar email"""

    def enviar(self, destino, mensaje):
        print(f"Enviando e-mail a {destino}: {mensaje}")


class EnviadorPush(CanalNotificaciones):
    """Clase: enviar push"""

    def enviar(self, destino, mensaje):
        print(f"Enviando PUSH a {destino}: {mensaje}")


class EnviadorSMS(CanalNotificaciones):
    """Clase: enviar SMS"""

    def enviar(self, destino, mensaje):
        print(f"Enviando SMS a {destino}: {mensaje}")

# Modulo de alto nivel (depende UNICAMENTE de la abstraccion)


class SistemaNotificaciones:
    """Clase: sistema de notificaciones"""

    def __init__(self, canales: List[CanalNotificaciones]):
        # Inyeccion de dependencias: recibe cualquier lista de "CanalNotificaciones"
        self._canales = list(canales)

    def agregar_canal(self, canal: CanalNotificaciones):
        """Funcion: agregar canal"""
        self._canales.append(canal)

    def notificar(self, destino, mensaje):
        """Funcion: notificar"""
        if not self._canales:
            raise RuntimeError("No hay canales configurados")
        for canal in self._canales:
            canal.enviar(destino, mensaje)


# 4) Comprobacion de que se cumple el principio (swap de implementaciones)
if __name__ == "__main__":
    # Podemos armar el sistema con cualquier combinacion de canales
    sistema_email_sms = SistemaNotificaciones([EnviadorEmail(), EnviadorSMS()])
    sistema_email_sms.notificar(
        "thouxivan@gmail.com", "Codigo de validacion: 123456")
    print("---- cambiar implementaciones sin tocar SistemaNotificaciones ----")
    sistema_push_solo = SistemaNotificaciones([EnviadorPush()])
    sistema_push_solo.notificar(
        "device-token-abc", "Tienes una nueva notificacion")
    print("---- agregar dinamicamente otro canal ----")
    sistema_push_solo.agregar_canal(EnviadorEmail())
    sistema_push_solo.notificar("device-token-abc", "Recordatorio de evento")

# SistemasNotificaciones no conoce EnviadorEmail, EnviadorPush, EnviadorSMS (solo conoce
# la abstraccion CanalNotificaciones)
# Podemos cambiar o agregar canales sin modificar SistemaNotificaciones -> cumple DIP
# La inyeccion de dependencias ocurre en el __init__ y con agregar_canal
# -------------------------------------------------------------------------------------
