from wordle import Wordle
from wordle_solver import WordleSolver

def main():
    wordle = Wordle()
    solver = WordleSolver()

    while not wordle.game_completed:
        solver.update_GYG(wordle.score_guess(solver.best_match(solver.find_matches())))

main()