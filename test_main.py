from unittest import TestCase
from main import Main

class TestMain(TestCase):
    def TestCaseForAlphabetDictDictionary(self):
        self.assertEqual(Main().AlphabetDict[2], ['a', 'b', 'c'])