import random
from word_list import *

class Wordle():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.answer: str = self.word_list[random.randrange(0, len(self.word_list))]
        self.guess_count: int = 0

    #compares the input guess to the correct answer    
    def score_guess(self, word: str) -> list[str]:
        if self.guess_count >= 6:
            return
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

        self.guess_count += 1
        result = ""
        for pos in score:
            result += f"{pos} "
        print(result)
        self.assert_win(score)

        return score

    #checks if the answer has been guessed and issues a loss if max guesses are reached
    def assert_win(self, score: list[str]) -> None:
        if self.guess_count >= 6 and score != ["G", "G", "G", "G", "G"]:
            print(f"\nTry again tomorrow..\n\nToday's word: {self.answer}")
        elif score == ["G", "G", "G", "G", "G"]:
            print(f"\nYou Win!\n\nToday's word: {self.answer}")
            self.guess_count = 7

