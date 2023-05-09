from unittest import TestCase

from sistema_controle_eletrico.motor import Motor

class TestMotor(TestCase):

    def test_verifica_motor_ligado(self):

    #     # Cria instancia da classe Motor
        motor = Motor()

    #     # Verifica se o objeto motor é da mesma classe Motor
        self.assertIsInstance(motor, Motor)
    #     # Por padrão, o motor inicial desligado, ou seja, zero
        self.assertEqual(motor.LIGADO, 0)

    #     # Após ligar o motor, o seu status deve ser um
        motor.inicia_motor()
        self.assertEqual(motor.LIGADO, 1)

    #     # Após desligar, o valor deve voltar a ser zero
        motor.desliga_motor()
        self.assertEqual(motor.LIGADO, 0)

    def test_calcula_potencia(self):

        motor = Motor()
        espereado = 36_955.53

        # Verifica caso potencia acima de 0.5
        potencia = motor.calcula_potencia(amperes=50, voltagem=1100, theta=0.834)
        self.assertAlmostEqual(potencia, espereado, places=2)

        potencia = motor.calcula_potencia(amperes=50, voltagem=1100, theta=0.2)
        self.assertGreaterEqual(motor.eficiencia, 0.5)

    def test_calcula_rotacoes_minuto(self):

        motor = Motor()

        potencia = motor.calcula_potencia(amperes=50, voltagem=1100, theta=0.834)

        rotacoes = motor.calcula_rotacoes_minuto(potencia)
        esperado = 1176.33

        self.assertAlmostEqual(rotacoes, esperado, places=2)
