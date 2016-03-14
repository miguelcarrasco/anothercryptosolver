import unittest

from anothercryptosolver.wordmodels import LetterPattern


class TestLetterPattern(unittest.TestCase):
    def test_generate_pattern(self):
        self.assertEqual('aba', LetterPattern.generate_pattern('ese'))
        self.assertEqual('ababa', LetterPattern.generate_pattern('esese'))
        self.assertEqual('ababac', LetterPattern.generate_pattern('esesel'))
        self.assertEqual('abcdefga', LetterPattern.generate_pattern('arboleda'))
