import unittest # Módulo estándar de Python para realizar pruebas unitarias.
from charfun import esPalindromo # Se importa la función esPalindromo desde el archivo charfun.py.

class TestPalindromo(unittest.TestCase):
    def test_anita_lava_la_tina(self):
        # Prueba la frase que ha sido dicha en el enunciado.
        self.assertTrue(esPalindromo("Anita lava la tina"))

    def test_cadena_vacia(self):
        # Prueba una cadena de texto vacía.
        self.assertTrue(esPalindromo(""))

    def test_solo_espacios(self):
        # Prueba una cadena de texto de solo espacios.
        self.assertTrue(esPalindromo("     "))

    def test_con_puntuacion(self):
        # Prueba una cadena de texto con puntuación.
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))

    def test_no_palindromo(self):
        # Prueba una cadena de texto que no es palindromo.
        self.assertFalse(esPalindromo("Esto no es un palíndromo"))

    def test_con_numeros(self):
        # Prueba con números tanto palíndromos como no palíndromos.
        self.assertTrue(esPalindromo("12756"))
        self.assertFalse(esPalindromo("12345"))

    def test_mayus_minus(self):
        # Prueba el cambio de mayúsculas y minúsculas.
        self.assertTrue(esPalindromo("Aa"))

if __name__ == "__main__":
    unittest.main()
