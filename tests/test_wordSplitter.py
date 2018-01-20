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


    def test_punctuation_swap(self):

        mapper = WordSplitter()
        punctuation_tuples = [("anti-hero.","anti-heroine."),("he's all that! and a bag of chips", "she's all that! and a bag of chips"), ("he`ll", "she`ll"), ("step-son", "step-daughter")]
        for tuple in punctuation_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)

