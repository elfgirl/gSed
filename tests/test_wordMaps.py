from unittest import TestCase
from gSed.wordMaps import WordMaps

class TestWordMaps(TestCase):
    def test_getRegexList(self):
        mapper = WordMaps()
        for type in ["complete", "start", "end","anywhere", "special"] :
            regex_map = mapper.getRegexList(type)
            self.assertIsNotNone(regex_map)

    def test_swap(self):

        mapper = WordMaps()
        gendered_tuples = [("She", "He"), ("He", "She"), ("man", "woman")]
        for tuple in gendered_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)

        nongendered_tuples = [("all", "all"), ("bastion", "bastion"), ("Clark", "Clark")]
        for tuple in nongendered_tuples :
            answer = mapper.swap(tuple[0])
            self.assertEqual(tuple[1], answer)