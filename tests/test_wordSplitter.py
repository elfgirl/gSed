from unittest import TestCase

from gSed.WordSplitter import WordSplitter

class TestWordSplitter(TestCase):
    def test_swap(self):
        splitter =  WordSplitter()
        gendered_phrases = [("So once there was a man from Nantucket.",
                    "So once there was a woman from Nantucket.")]
        for phrase in gendered_phrases :

            response = splitter.swap(phrase[0])
            self.assertEqual(phrase[1], response)

