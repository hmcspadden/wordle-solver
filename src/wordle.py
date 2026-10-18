import random
from word_list import *

class Wordle():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.answer: str = self.word_list[random.randrange(0, len(self.word_list))]
        self.guess_count: int = 0
        
        
    def score_guess(self, word: str) -> list[str]:
        score = []
        for i in range(len(word)):
            if word[i] == self.answer[i]:
                score.append("G")
            elif word[i] in self.answer:
                score.append("Y")
            else:
                score.append("X")

        return score