import unittest
import os
from build_trie import *

class TestTrieBuilder(unittest.TestCase):
    def test_reader(self):
        reader = read_text("./assets/data/valid-wordle-words.txt")
        
    def test_build_trie(self):
        build_trie("./assets/data/valid-wordle-words.txt")

    def test_json_to_trie(self):
        trie1 = json_to_trie("./assets/data/valid-wordle-words.txt")
        
            

if __name__ == '__main__':
    unittest.main()

