from word_list import *

class WordleSolver():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.pos_char_freq: list[list[str]] = positional_char_frequency(self.word_list)
        self.current_word: str | None = None
        self.green: dict[int, str] = {}
        self.yellow: dict[str, list[int]] = {}
        self.grey: list[str] = []

    #find matches in the word list based on current guess state
    def find_matches(self) -> list[str]:
        matches = []

        for word in self.word_list:
            if len(word) != 5:
                continue
            match = True

            #check for established correct guesses
            for pos, char in self.green.items():
                if word[pos] != char:
                    match = False
                    break
            if not match:
                continue
            
            #check if char in incorrect guesses
            for char in word:
                if char in self.grey:
                    match = False
                    break
            if not match:
                continue

            #check if word has char in pos of yellow
            for char, positions in self.yellow.items():
                if char in word and word.index(char) not in positions:
                    match = False
                    break
            if not match:
                continue

            matches.append(word)

        return matches

    #finds the word with highest positional score in a word list
    def best_match(self, words: list[str]) -> str:
        word_scores = {}

        for word in words:
            score = 0

            #calculate positional score for each letter and add total word score
            for i in range(len(word)):
                score += 26 - self.pos_char_freq[i].index(word[i])

            word_scores[word] = score

        highest_score = max(word_scores, key=word_scores.get)
        
        return highest_score
            