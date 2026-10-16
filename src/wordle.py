import random
from word_list import *

class Wordle():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.answer: str = ""
        self.guess_count: int = 0
        