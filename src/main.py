from wordle import Wordle
from wordle_solver import WordleSolver

def main():
    wordle = Wordle()
    solver = WordleSolver()
    wordle.answer = "stink"

    while wordle.guess_count < 6:
        solver.update_GYG(wordle.score_guess(solver.best_match(solver.find_matches())))

main()