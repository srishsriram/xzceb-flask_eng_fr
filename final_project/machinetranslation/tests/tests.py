import unittest
import json
from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def testNull(self):
        self.assertEqual(frenchToEnglish(""),"")

    def testBonjour(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

class TestEnglishToFrench(unittest.TestCase):
    def testNull(self):
        self.assertEqual(englishToFrench(""),"")

    def testHello(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

unittest.main()