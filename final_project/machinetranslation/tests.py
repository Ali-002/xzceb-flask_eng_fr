import unittest
  
from translator import EnglishToFrench, FrenchToEnglish

class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(EnglishToFrench('Hello'), 'Bonjour')

class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(FrenchToEnglish('Bonjour'), 'Hello')

unittest.main()
