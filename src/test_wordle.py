import unittest
from wordle import *
from wordle_solver import WordleSolver

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

        wordle4 = Wordle()
        wordle4.answer = "booze"
        self.assertEqual(["X", "G", "X", "X", "Y"], wordle4.score_guess("condo"))

    def test_assert_win(self):
        wordle = Wordle()
        solver = WordleSolver()
        wordle.guess_count = 5
        wordle.score_guess(solver.best_match(solver.find_matches()))

        wordle.guess_count = 2
        wordle.score_guess(wordle.answer)


if __name__ == '__main__':
    unittest.main()
