import unittest
from wordle_solver import WordleSolver
from wordle import Wordle

class TestWordleSolver(unittest.TestCase):
    def test_match_green(self):
        solver = WordleSolver()
        solver.green = {0 : "s", 1 : "t", 2 : "a", 3 : "r", 4 : "e"}
        self.assertEqual(["stare"], solver.find_matches())

        solver2 = WordleSolver()
        solver2.green = {0 : "s", 1 : "t", 2 : "a", 3 : "r", 4 : "e"}
        solver2.grey = ["a", "e"]
        self.assertEqual(["stare"], solver2.find_matches())

    def test_grey(self):
        solver = WordleSolver()
        solver.grey = ["a", "e", "i", "o", "u"]
        #print(solver.find_matches())

    def test_match_yellows(self):
        solver = WordleSolver()
        solver.green = {0 : "c"}
        solver.yellow = {"a" : [2, 4]}
        solver.grey = ["i", "o", "u", "y", "e"]
        #print(solver.find_matches())

        solver2 = WordleSolver()
        solver2.green = {0 : "p", 4 : "e"}
        solver2.yellow = {"e" : [1]}
        #print(solver2.find_matches())

    def test_best_match(self):
        solver = WordleSolver()
        matches = solver.find_matches()
        #print(solver.best_match(matches))

    def test_update_gyg(self):
        solver = WordleSolver()
        wordle = Wordle()
        wordle.answer = "stare"
        first_guess = solver.best_match(solver.find_matches())
        solver.update_GYG(wordle.score_guess(first_guess))
        self.assertEqual(
            {2 : "a", 4 : "e"},
            solver.green
        )
        self.assertEqual(
            {"r" : [1]},
            solver.yellow
        )
        self.assertEqual(
            ["c", "n"],
            solver.grey
        )

if __name__ == '__main__':
    unittest.main()
