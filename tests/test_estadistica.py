# file: tests/test_estadistica.py
import unittest
from scr.logica.estadistica import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular

class PruebaEstadistica(unittest.TestCase):

    # Pruebas para calcular_media
    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    def test_media_dos_elementos(self):
        self.assertEqual(calcular_media([4, 6]), 5)

    def test_media_n_elementos_positivos(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)

    def test_media_n_elementos_ceros(self):
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_n_elementos_positivos_y_negativos(self):
        self.assertEqual(calcular_media([-2, -1, 0, 1, 2]), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_media([1, "a", 3])

    # Pruebas para calcular_desviacion_estandar
    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0.0)

    def test_desviacion_estandar_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([4, 6]), 1.0)

    def test_desviacion_estandar_n_elementos_positivos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), 1.414213562)

    def test_desviacion_estandar_n_elementos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0]), 0.0)

    def test_desviacion_estandar_n_elementos_positivos_y_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([-2, -1, 0, 1, 2]), 1.414213562)

    def test_desviacion_estandar_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([1, "a", 3])

if __name__ == '__main__':
    unittest.main()
