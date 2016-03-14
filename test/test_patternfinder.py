# -*- coding: utf-8 -*-

import unittest

from anothercryptosolver.patternsearching import PatternFinder


class TestDictUtils(unittest.TestCase):
    def test_dict_compatible(self):
        ciphered = 'xtx'
        substitution_word = 'ese'
        dict = {'x': 'e'}
        self.assertTrue(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))

        ciphered = 'xtx'
        substitution_word = 'ese'
        dict = {'x': 'e', 't': 's'}
        self.assertTrue(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))

        ciphered = 'xtx'
        substitution_word = 'ese'
        dict = {'x': 'e', 't': 'f'}
        self.assertFalse(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))

        ciphered = 'xtx'
        substitution_word = 'ese'
        dict = {}
        self.assertTrue(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))

        ciphered = 'xtx'
        substitution_word = 'eses'
        dict = {}
        self.assertFalse(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))

        ciphered = 'xtx'
        substitution_word = 'ese'
        dict = {'x': 'e', 'n': 's'}
        self.assertFalse(PatternFinder.is_dict_compatible(ciphered, substitution_word, dict))
