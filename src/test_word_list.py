import unittest
from word_list import *

class TestWordList(unittest.TestCase):
    def test_build_list(self):
        build_word_list("./assets/data/valid-wordle-words.txt")

    def test_word_freq(self):
        positional_char_frequency(build_word_list("./assets/data/valid-wordle-words.txt"))

if __name__ == '__main__':
    unittest.main()
