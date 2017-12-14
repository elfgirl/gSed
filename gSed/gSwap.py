import json

import wordSplitter


class gSwap:
    def __init__(self):
        self.word_splitter = wordSplitter.wordSplitter()

    def swap(self, page):
        return self.word_splitter.swap(page)

    def contexts_performed(self):
        return json.dumps(self.word_splitter.contexts, sort_keys=True, indent=4, default=str)

    def swaps_perfomed(self):
        return json.dumps(self.word_splitter.swaps, sort_keys=True, indent=4, default=str)

    def repair(self):
        #TODO repair common mistakes
        pass