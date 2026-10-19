import random
from word_list import *

class Wordle():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.answer: str = self.word_list[random.randrange(0, len(self.word_list))]
        self.guess_count: int = 0

    #compares the input guess to the correct answer    
    def score_guess(self, word: str) -> list[str]:
        score = []
        char_count = {} #variable to keep track of double letter guesses

        #first loop compares marks green values and count correct chars
        for i in range(len(word)):
            if word[i] not in char_count:
                char_count[word[i]] = 0
            if word[i] == self.answer[i]:
                score.append("G")
                char_count[word[i]] += 1
            else:
                score.append(None)
            
        #second loop assigns yellow/grey on remaining chars 
        for i in range(len(word)):
            if score[i] == "G":
                continue
            elif word[i] not in self.answer:
                score[i] = "X"
            elif word[i] in self.answer and self.answer.count(word[i]) <= char_count[word[i]]:
                score[i] = "X"
            else:
                score[i] = "Y"
                char_count[word[i]] += 1

        return score