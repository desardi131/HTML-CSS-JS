import unittest
from funciones import es_primo

class TestEs_primo(unittest.TestCase):
    def test_es_primo(self):
        print('-----Test valores de resultado conocido')
        self.assertRaises(TypeError,es_primo,13.4)
        self.assertRaises(TypeError,es_primo,'hola')
        self.assertRaises(TypeError,es_primo,2+3j)
        self.assertRaises(TypeError,es_primo,True)
