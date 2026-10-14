import os
import json
from trie import Trie


def read_text(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")

    with open(filepath, "r") as f:
        text = f.read()

    return text


def build_trie(filepath: str) -> Trie:
    text = read_text(filepath)
    words = text.split("\n")
    word_list = Trie()

    for word in words:
        word_list.add(word)

    return word_list


def trie_to_jason(word_list: Trie) -> None:
    with open("./assets/data/word_list.json", "w") as f:
        json.dump(word_list.root, f)


def json_to_trie(filepath: str) -> Trie:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")

    word_list = Trie()
    with open(filepath, "r") as f:
        word_list.set_root(json.load(f))

    return word_list