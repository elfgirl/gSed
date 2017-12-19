import json
from unittest import TestCase

from gSed.gSwap import gSwap

sample_texts = {
        u"On The Road (Jack Kerouac)":
            (
                u"I first met Dean not long after my wife and I split up. I had just gotten over a serious illness that I won't bother to talk about, except that it had something to do with the miserably weary split-up and my feeling that everything was dead. With the coming of Dean Moriarty began the part of my life you could call my life on the road. Before that I'd often dreamed of going West to see the country, always vaguely planning and never taking off. Dean is the perfect guy for the road because he actually was born on the road, when his parents were passing through Salt Lake City in 1926, in a jalopy, on their way to Los Angeles. First reports of him came to me through Chad King, who'd shown me a few letters from him written in a New Mexico reform school. I was tremendously interested in the letters because they so naively and sweetly asked Chad to teach him all about Nietzsche and all the wonderful intellectual things that Chad knew. At one point Carlo and I talked about the letters and wondered if we would ever meet the strange Dean Moriarty. This is all far back, when Dean was not the way he is today, when he was a young jailkid shrouded in mystery. Then news came that Dean was out of reform school and was coming to New York for the first time; also there was talk that he had just married a girl called Marylou.",
                u"I first met Dean not long after my husband and I split up. I had just gotten over a serious illness that I won't bother to talk about, except that it had something to do with the miserably weary split-up and my feeling that everything was dead. With the coming of Dean Moriarty began the part of my life you could call my life on the road. Before that I'd often dreamed of going West to see the country, always vaguely planning and never taking off. Dean is the perfect gal for the road because she actually was born on the road, when her parents were passing through Salt Lake City in 1926, in a jalopy, on their way to Los Angeles. First reports of her came to me through Chad Queen, who'd shown me a few letters from her written in a New Mexico reform school. I was tremendously interested in the letters because they so naively and sweetly asked Chad to teach her all about Nietzsche and all the wonderful intellectual things that Chad knew. At one point Carlo and I talked about the letters and wondered if we would ever meet the strange Dean Moriarty. This is all far back, when Dean was not the way she is today, when she was a young jailkid shrouded in mystery. Then news came that Dean was out of reform school and was coming to New York for the first time; also there was talk that she had just married a boy called Marylou."),

        u"Pride & Prejudice (Jane Austen)":
            (
                u"It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
                u"It is a truth universally acknowledged, that a single woman in possession of a good fortune must be in want of a husband. However little known the feelings or views of such a woman may be on her first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that she is considered as the rightful property of some one or other of their sons."),

        u"Metamorphosis (Franz Kafka)":
            (
                u"As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect. He was lying on his hard, as it were armor-plated, back and when he lifted his head a little he could see his dome-like brown belly divided into stiff arched segments on top of which the bed quilt could hardly keep in position and was about to slide off completely. His numerous legs, which were pitifully thin compared to the rest of his bulk, waved helplessly before his eyes.",
                u"As Gregor Samsa awoke one morning from uneasy dreams she found herself transformed in her bed into a gigantic insect. She was lying on her hard, as it were armor-plated, back and when she lifted her head a little she could see her dome-like brown belly divided into stiff arched segments on top of which the bed quilt could hardly keep in position and was about to slide off completely. Her numerous legs, which were pitifully thin compared to the rest of her bulk, waved helplessly before her eyes."),

        u"Invisible Man (Ralph Ellison)":
            (
                u"I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; nor am I one of your Hollywood-movie ectoplasms. I am a man of substance, of flesh and bone, fiber and liquids-and I might even be said to possess a mind. I am invisible, understand, simply because people refuse to see me. Like the bodiless heads you see sometimes in circus sideshows, it is as though I have been surrounded by mirrors of hard, distorting glass. When they approach me they see only my surroundings, themselves, or figments of their imagination-indeed, everything and anything except me.",
                u"I am an invisible woman. No, I am not a spook like those who haunted Edgar Allan Poe; nor am I one of your Hollywood-movie ectoplasms. I am a woman of substance, of flesh and bone, fiber and liquids-and I might even be said to possess a mind. I am invisible, understand, simply because people refuse to see me. Like the bodiless heads you see sometimes in circus sideshows, it is as though I have been surrounded by mirrors of hard, distorting glass. When they approach me they see only my surroundings, themselves, or figments of their imagination-indeed, everything and anything except me."),
    }


class TestGSwap(TestCase):


    def test_swap(self):
        self.maxDiff = None
        splitter = gSwap()

        for surce, text in sample_texts.iteritems():
            response = splitter.swap(text[0])
            self.assertEqual(text[1], response)

    def test_contexts_performed(self):
        self.maxDiff = None
        splitter = gSwap()

        for surce, text in sample_texts.iteritems():
            response = splitter.swap(text[0])
            self.assertEqual(text[1], response)

        contexts = {
            u'I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; nor am I one of your Hollywood-movie ectoplasms. I am a man of substance, of flesh and bone, fiber and liquids-and I might even be said to possess a mind. I am invisible, understand, simply because people refuse to see me. Like the bodiless heads you see sometimes in circus sideshows, it is as though I have been surrounded by mirrors of hard, distorting glass. When they approach me they see only my surroundings, themselves, or figments of their imagination-indeed, everything and anything except me.': [
                {u'source': u'man', u'flip': u'woman'}, {u'source': u'man', u'flip': u'woman'}],
            u'As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect. He was lying on his hard, as it were armor-plated, back and when he lifted his head a little he could see his dome-like brown belly divided into stiff arched segments on top of which the bed quilt could hardly keep in position and was about to slide off completely. His numerous legs, which were pitifully thin compared to the rest of his bulk, waved helplessly before his eyes.': [
                {u'source': u'he', u'flip': u'she'}, {u'source': u'himself', u'flip': u'herself'},
                {u'source': u'his', u'flip': u'her'}, {u'source': u'He', u'flip': u'She'},
                {u'source': u'his', u'flip': u'her'}, {u'source': u'he', u'flip': u'she'},
                {u'source': u'his', u'flip': u'her'}, {u'source': u'he', u'flip': u'she'},
                {u'source': u'his', u'flip': u'her'}, {u'source': u'His', u'flip': u'Her'},
                {u'source': u'his', u'flip': u'her'}, {u'source': u'his', u'flip': u'her'}],
            u"I first met Dean not long after my wife and I split up. I had just gotten over a serious illness that I won't bother to talk about, except that it had something to do with the miserably weary split-up and my feeling that everything was dead. With the coming of Dean Moriarty began the part of my life you could call my life on the road. Before that I'd often dreamed of going West to see the country, always vaguely planning and never taking off. Dean is the perfect guy for the road because he actually was born on the road, when his parents were passing through Salt Lake City in 1926, in a jalopy, on their way to Los Angeles. First reports of him came to me through Chad King, who'd shown me a few letters from him written in a New Mexico reform school. I was tremendously interested in the letters because they so naively and sweetly asked Chad to teach him all about Nietzsche and all the wonderful intellectual things that Chad knew. At one point Carlo and I talked about the letters and wondered if we would ever meet the strange Dean Moriarty. This is all far back, when Dean was not the way he is today, when he was a young jailkid shrouded in mystery. Then news came that Dean was out of reform school and was coming to New York for the first time; also there was talk that he had just married a girl called Marylou.": [
                {u'source': u'wife', u'flip': u'husband'}, {u'source': u'guy', u'flip': u'gal'},
                {u'source': u'he', u'flip': u'she'}, {u'source': u'his', u'flip': u'her'},
                {u'source': u'him', u'flip': u'her'}, {u'source': u'King', u'flip': u'Queen'},
                {u'source': u'him', u'flip': u'her'}, {u'source': u'him', u'flip': u'her'},
                {u'source': u'he', u'flip': u'she'}, {u'source': u'he', u'flip': u'she'},
                {u'source': u'he', u'flip': u'she'}, {u'source': u'girl', u'flip': u'boy'}],
            u'It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.': [
                {u'source': u'man', u'flip': u'woman'}, {u'source': u'wife', u'flip': u'husband'},
                {u'source': u'man', u'flip': u'woman'}, {u'source': u'his', u'flip': u'her'},
                {u'source': u'he', u'flip': u'she'}, {u'source': u'daughters', u'flip': u'sons'}]}
        performed = json.loads(splitter.contexts_performed())
        self.assertEqual(contexts, performed)

    def test_swaps_performed(self):
        self.maxDiff = None
        splitter = gSwap()

        for surce, text in sample_texts.iteritems():
            response = splitter.swap(text[0])
            self.assertEqual(text[1], response)

        swaps = {u'King': u'Queen', u'his': u'her', u'His': u'Her', u'wife': u'husband', u'him': u'her',
                 u'himself': u'herself', u'man': u'woman', u'girl': u'boy', u'he': u'she', u'guy': u'gal',
                 u'daughters': u'sons', u'He': u'She'}
        performed = json.loads(splitter.swaps_performed())
        self.assertEqual(swaps, performed)

    def test_repair(self):
        pass


