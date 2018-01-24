import re

import wordMaps


class WordSplitter:
    def __init__(self):
        self.word_mapper = wordMaps.WordMaps()

        self.word_breaker = re.compile(r"([^\W\d]*)", re.MULTILINE)
        self.sentence_breaker = re.compile(r"((?!=|\!|\.|\?).)+.\b", re.MULTILINE)

        self.swaps = {}
        self.contexts = {}

    def swap(self, text_block=""):

        new_text_block = []

        sentence_end_position = 0
        for sentence_match in self.sentence_breaker.finditer(text_block):
            # Run through word based swaps first

            new_sentance = []
            sentence_span = sentence_match.span()
            # Collect Punctuation and whitespace till next sentence
            if sentence_span[0] != sentence_end_position:
                new_text_block.append(text_block[sentence_end_position:sentence_span[0]])
                sentence_end_position = sentence_span[0]
            source_sentence = text_block[sentence_span[0]:sentence_span[1]]

            last_word_position = 0
            for word_match in self.word_breaker.finditer(source_sentence):
                word_span = word_match.span()
                if word_span[0] == word_span[1]:
                    # blank match. TODO improve regex
                    continue
                # Collect Whitespace till next match
                if word_span[0] != last_word_position:
                    new_sentance.append(source_sentence[last_word_position:word_span[0]])
                source_word = source_sentence[word_span[0]:word_span[1]]

                word = self.word_mapper.swap(source_word)
                new_sentance.append(word)
                last_word_position = word_span[1]

                if word != source_word:
                    self.swaps[source_word] = word
                    if not source_sentence in self.contexts:
                        self.contexts[source_sentence] = []
                    self.contexts[source_sentence].append({'source': source_word, 'flip': word, })


            new_text_block.append("".join(new_sentance))
            sentence_end_position = sentence_span[1]

        # Collect final punctuations
        if sentence_end_position != len(text_block):
            new_text_block.append(text_block[sentence_end_position:])
        return "".join(new_text_block)
