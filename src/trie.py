from typing import Any

class Trie:
    def __init__(self) -> None:
        self.root: dict[str, Any] = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

    def search_level(
        self, current_level: dict[str, Any], current_prefix: str, words: list[str]
    ) -> list[str]:
        if self.end_symbol in current_level:
            words.append(current_prefix)
        chars = current_level.keys()
        for char in sorted(chars):
            print(char == self.end_symbol)
            if char != self.end_symbol:
                new_prefix = current_prefix + char
                self.search_level(current_level[char], new_prefix, words)
        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        match = []
        level = self.root
        for char in prefix:
            if char not in level:
                return []
            level = level[char]
        return self.search_level(level, prefix, match)

    def find_matches(self, document: str) -> set[str]:
        matches = set()

        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                if document[j] not in level:
                    break
                else:
                    level = level[document[j]]
                if self.end_symbol in level:
                    matches.add(document[i:j + 1])
        return matches

    def longest_common_prefix(self) -> str:
        level = self.root
        prefix = ""
        while True:
            children = []
            for key in level.keys():
                if key != self.end_symbol:
                    children.append(key)
            if self.end_symbol in level or len(children) != 1:
                break
            prefix += children[0]
            level = level[children[0]]
        return prefix

    def set_root(self, words_list: dict[str, Any]) -> None:
        self.root = words_list