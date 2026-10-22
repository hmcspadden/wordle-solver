from wordle import Wordle
from wordle_solver import WordleSolver

def every_word():
    count = 0
    guesses = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0
    }

    wordle = Wordle()
    for word in wordle.word_list:
        wordle.answer = word
        wordle.guess_count = 0
        wordle.game_completed = False
        solver = WordleSolver()

        while not wordle.game_completed:
            solver.update_GYG(wordle.score_guess(solver.best_match(solver.find_matches())))

        count += 1
        guesses[wordle.guess_count] += 1

    total = 0
    for key, value in guesses.items():
        total += key * value

    print(guesses)
    print(f"\nAVG: {total / count}")

every_word()