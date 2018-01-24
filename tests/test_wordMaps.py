from unittest import TestCase
from gSed.wordMaps import WordMaps

class TestWordMaps(TestCase):

    def test_gendered_swap(self):

        mapper = WordMaps()
        gendered_tuples = [("She", "He"), ("He", "She"), ("man", "woman"), ("airman","airwoman"),("airmen","airwomen"), ("boyhood", "girlhood"),("boyhoods", "girlhoods")]
        for tuple in gendered_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)

    def test_non_gendered_swap(self):

        mapper = WordMaps()
        nongendered_tuples = [("all", "all"), ("bastion", "bastion"), ("Clark", "Clark")]
        for tuple in nongendered_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)

    def test_suffix_swap(self):

        mapper = WordMaps()
        suffix_tuples = [("airman","airwoman"),("airmen","airwomen")]
        for tuple in suffix_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)

    def test_prefix_swap(self):

        mapper = WordMaps()
        prefix_tuples = [("patriarchal", "matriarchal")]
        for tuple in prefix_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)


    def test_edge_case_swap(self):

        mapper = WordMaps()
        gendered_tuples = [("", ""), (" ", " "), (".", "."), (";:",";:")]
        for tuple in gendered_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)
