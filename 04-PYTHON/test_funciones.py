import unittest
from funciones import es_primo

class TestEs_primo(unittest.TestCase):
    # Test de valores conocidos, debemos introducir valores que sabemos que la solucion es correcta
    def test_es_primo(self):
        print('-----Test valores de resultado conocido')

        self.assertAlmostEqual(es_primo(5),True)
        self.assertAlmostEqual(es_primo(6),False)
        self.assertAlmostEqual(es_primo(31),True)
        self.assertAlmostEqual(es_primo(15),False)

    # Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos----')
    #Indicamos el tipo de excepción, la función y el valor esperado.

        self.assertRaises(ValueError,es_primo,-12)
        self.assertRaises(ValueError,es_primo,0)
        self.assertRaises(ValueError,es_primo,-31)
    
    # Test de tipos no compatibles. Verificamos si el tipo de los parámetros es el correcto
    # El tipo de la excepcion debe ser TypeError
    # Hacemos una prueba para cada tipo conocido no válido
    def test_tipos(self):
        print('-----Test de tipos no compatibles----')

        self.assertRaises(TypeError,es_primo,True)
        self.assertRaises(TypeError,es_primo,'Hola')
        self.assertRaises(TypeError,es_primo,2+3j)
        self.assertRaises(TypeError,es_primo,12.5)