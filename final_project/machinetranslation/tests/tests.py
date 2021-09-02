import unittest

import translator as tr

class TestTranslator(unittest.TestCase):

    def test_english_to_french_null(self):
        self.assertEqual(tr.english_to_french(), "", 'Should be ""')
    
    def test_french_to_english_null(self):
        self.assertEqual(tr.french_to_english(), "", 'Should be ""')
    
    def test_english_to_french_assertEqual(self):
        self.assertEqual(tr.english_to_french("Hello"), "Bonjour", "Should be 'Bonjour'")
    
    def test_english_to_french_assertNotEqual(self):
        self.assertNotEqual(tr.english_to_french("Hello"), "Hello", "Should be 'Bonjour'")
    
    def test_french_to_english_assertEqual(self):
        self.assertEqual(tr.french_to_english("Bonjour"), "Hello", "Should be 'Hello'")
    
    def test_french_to_english_assertNotEqual(self):
        self.assertNotEqual(tr.french_to_english("Bonjour"), "Bonjour", "Should be 'Hello'")

if __name__ == '__main__':
    unittest.main()
