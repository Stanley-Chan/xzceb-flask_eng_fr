import unittest
from translator import french_to_english, english_to_french

class test_fr_to_en(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test translation
        self.assertNotEqual(french_to_english("null"), "null") # test for null input
        
class test_eng_to_fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test translation
        self.assertNotEqual(english_to_french("null"), "null") # test for null input
                
unittest.main()