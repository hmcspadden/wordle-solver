import unittest
from wordle_solver import WordleSolver

class TestWordleSolver(unittest.TestCase):
    def test_match_green(self):
        solver = WordleSolver()
        solver.green = {0 : "s", 1 : "t", 2 : "a", 3 : "r", 4 : "e"}
        print(solver.find_matches())
        self.assertEqual(["stare"], solver.find_matches())

    def test_grey(self):
        solver = WordleSolver()
        solver.grey = ["a", "e", "i", "o", "u"]
        print(solver.find_matches())

    def test_match_yellows(self):
        solver = WordleSolver()
        solver.yellow = {"a" : [2, 4], "e" : [2, 4]}
        solver.grey = ["i", "o", "u", "y"]
        print(solver.find_matches())

if __name__ == '__main__':
    unittest.main()
