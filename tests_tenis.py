import unittest

from partido_tenis import Puntos


class PartidoTenis(unittest.TestCase):
    puntos = Puntos()


    def test_inicio_partida(self):
        set = [(0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = self.puntos.calcularResultado(set)
        self.assertEqual(resultado, "0-0")

    def test_15_a_0(self):
        set = [(1, 0), (0, 0), (0, 0), (0, 0)]
        resultado = self.puntos.calcularResultado(set)
        self.assertEqual(resultado, "15-0")
