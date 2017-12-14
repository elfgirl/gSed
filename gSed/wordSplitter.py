import re

import wordMaps


class wordSplitter:
    def __init__(self):
        self.mapper = wordMaps.wordmaps()
        self.swaps = {}
        self.contexts = {}

    # words = re.compile(r"([^\W\d](\w|[-']{1,2}(?=\w))*)", re.MULTILINE)
    def swap(self, text_block=""):
        word_breaker = re.compile(r"([^\W\d](\w|(?=\w))*)", re.MULTILINE)
        new_text_block = []
        last_end_position = 0

        for match in word_breaker.finditer(text_block):
            word_span = match.span()
            if word_span[0] != last_end_position:
                new_text_block.append(text_block[last_end_position:word_span[0]])
            source_word = text_block[word_span[0]:word_span[1]]
            word = self.mapper.swap(source_word)
            new_text_block.append(word)

            if word != source_word:
                self.swaps[source_word] = word
                if not text_block in self.contexts:
                    self.contexts[text_block] = []
                self.contexts[text_block].append({'source': source_word, 'flip': word, })
            last_end_position = word_span[1]

        if last_end_position != len(text_block):
            new_text_block.append(text_block[last_end_position:])

        return "".join(new_text_block),
