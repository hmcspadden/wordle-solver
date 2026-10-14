import unittest
from build_trie import *

class TestTrieBuilder(unittest.TestCase):
    def test_reader(self):
        reader = read_text("./valid-wordle-words.txt")
        print(reader)

if __name__ == '__main__':
    unittest.main()

