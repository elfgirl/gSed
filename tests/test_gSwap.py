from unittest import TestCase

from gSed.gSwap import gSwap

class TestGSwap(TestCase):
    def test_swap(self):

        splitter =  gSwap()
        phrases = [("So once there was a man from Nantucket.",
                    "So once there was a woman from Nantucket.")]
        for phrase in phrases :
            response = splitter.swap(phrase[0])
            self.assertEqual(phrase[1], response)


    def test_contexts_performed(self):
        self.fail()

    def test_swaps_performed(self):
        self.fail()

    def test_repair(self):
        pass
