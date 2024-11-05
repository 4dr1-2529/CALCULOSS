import unittest
from SRC.calculos_estadisticos import CalculosEstadisticos


class TestCalculosEstadisticos(unittest.TestCase):
    def setUp(self):
        self.calculos = CalculosEstadisticos()

    def tearDown(self):
        self.calculos = None

    def test_calcular_media(self):

        num = [1, 2, 3, 4, 5]
        resultado_esperado = 3.0
        resultado_actual = self.calculos.calcular_media(num)
        self.assertEqual(resultado_esperado, resultado_actual)


        num = [10, 20, 30, 40, 50]
        resultado_esperado = 30.0
        resultado_actual = self.calculos.calcular_media(num)
        self.assertEqual(resultado_esperado, resultado_actual)

    def test_calcular_desviacion_estandar(self):

        num = [1, 2, 3, 4, 5]
        resultado_esperado = 1.58
        resultado_actual = self.calculos.calcular_desviacion_estandar(num)
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)


        num = [10, 20, 30, 40, 50]
        resultado_esperado = 15.81
        resultado_actual = self.calculos.calcular_desviacion_estandar(num)
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)


        num = []
        resultado_actual = self.calculos.calcular_desviacion_estandar(num)
        self.assertIsNone(resultado_actual)


if __name__ == '__main__':
    unittest.main()
