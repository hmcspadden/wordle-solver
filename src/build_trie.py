import sys
import os

def read_text(filepath: str) -> list[str]:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")

    with open(filepath, "r") as f:
        text = f.read()
        word_list = text.split("\n")
    
    return word_list


def build_trie(word_list: list[str]) -> dict[str : str]:
    new_trie = {}

    for word in word_list:
        for i in range(len(word)):
            
            if i == 0 and new_trie[word[i]] != {}:
                new_trie[word[i]] = {}
            

            

    return new_trie