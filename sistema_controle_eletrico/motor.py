import time
import math
import random

from rich.console import Console

console = Console(color_system='truecolor')

PI = math.pi

class Motor:

    VOLTAGEM_BASE = 127.2
    TORQUE = 300
    LIGADO = 0

    amperes:int = 50
    rotacoes:float = 0.0
    potencia:float = 0.0
    voltagem:float = 0.0
    eficiencia:float = 0.0

    def calcula_potencia(self, voltagem: float, amperes: float, theta: float = 0.5) -> float:
        amperes = float(amperes)
        voltagem = float(voltagem)

        if (theta <= 0.5):
            theta = random.random() * 0.5 + 0.5

        self.eficiencia = theta
        cos_theta = math.cos(theta)

        return voltagem * amperes * cos_theta

    def calcula_rotacoes_minuto(self, potencia: float) -> float:

        return float(60 * potencia) / ((2 * PI) * self.TORQUE)

    def run(self):
        voltagem = random.randint(1000, 1100) + random.random()
        self.voltagem = voltagem

        potencia = self.calcula_potencia(voltagem, self.amperes)
        self.potencia = potencia

        rotacoes = self.calcula_rotacoes_minuto(potencia)
        self.rotacoes = rotacoes

    def inicia_motor(self, _loop:bool = False):

        self.LIGADO = 1

        if _loop is False:
            self.run()
            return

        if _loop is True:
            while self.LIGADO == 1:
                self.run()
                time.sleep(0.1)

    def desliga_motor(self):
        self.LIGADO = 0
