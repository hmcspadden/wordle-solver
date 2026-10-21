from word_list import *

class WordleSolver():
    def __init__(self):
        self.word_list: list[str] = build_word_list("./assets/data/wordle-answers.txt")
        self.char_freq: dict [str, int] = char_frequency(self.word_list)
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
                if char in self.grey and char not in self.green.values():
                    match = False
                    break
                elif char in self.grey and word.count(char) > str(self.green.values()).count(char):
                    match = False
                    break
            if not match:
                continue

            #check if word has char in pos of yellow
            for char, positions in self.yellow.items():
                if word.count(char) > 0:
                    for i in range(len(word)):
                        if char == word[i] and i in positions:
                            match = False
                            break
            if not match:
                continue

            #check if word has yellow that are not yet green
            if len(self.yellow) > 0:
                for char in self.yellow:
                    if char in self.green.values():
                        continue
                    if char not in word:
                        match = False
                        break
            if not match:
                continue

            
            matches.append(word)

        return matches

    def word_score(self, words: list[str]) -> dict[str, int]:
        word_scores = {}

        for word in words:
            score = 0

            #calculate positional score for each letter and add total word score
            for i in range(len(word)):
                score += 26 - self.pos_char_freq[i].index(word[i])

            word_scores[word] = score
        
        top_five = dict(sorted(word_scores.items(), key=lambda x: x[1], reverse=True)[:5])

        return top_five


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
        self.current_word = highest_score
        print(f"\n{highest_score}")
        
        return highest_score

    #updates green, yellow, grey fields based on scored guess
    def update_GYG(self, score: list[str]) -> None:
        for i in range(len(score)):
            if score[i] == "G":
                self.green[i] = self.current_word[i]
            elif score[i] == "Y":
                if self.current_word[i] not in self.yellow:
                    self.yellow[self.current_word[i]] = []
                self.yellow[self.current_word[i]].append(i)
            else:
                self.grey.append(self.current_word[i])

    
            