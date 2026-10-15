from word_list import *

class WordleSolver():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/valid-wordle-words.txt")
        self.pos_char_freq: list[list[str]] = positional_char_frequency(self.word_list)
        self.current_word: str | None = None
        self.green: dict[int, str] = {}
        self.yellow: dict[str, list[int]] = {}
        self.grey: list[str] = []

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

            