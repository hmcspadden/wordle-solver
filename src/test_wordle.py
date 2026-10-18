import unittest
from wordle import *

class TestWordle(unittest.TestCase):
    def test_init(self):
        wordle = Wordle()
        #print(wordle.answer)

    def test_score_guess(self):
        wordle = Wordle()
        wordle.answer = "valet"
        self.assertEqual(["X", "G", "Y", "G", "X"], wordle.score_guess("water"))
        
        wordle2 = Wordle()
        wordle2.answer = "peeve"
        self.assertEqual(["G", "X", "X", "Y", "G"], wordle2.score_guess("puree"))

        wordle3 = Wordle()
        wordle3.answer = "prone"
        self.assertEqual(["G", "X", "Y", "X", "G"], wordle3.score_guess("puree"))

if __name__ == '__main__':
    unittest.main()
