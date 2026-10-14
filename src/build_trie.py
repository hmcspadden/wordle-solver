import sys
import os

def read_text(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")

    with open(filepath, "r") as f:
        text = f.read()

    return text


def build_trie(text: list[str]) -> dict[str : str]:
    new_trie = {}

    if len(text) > 5:
        text = text.split("")
            

            

    return new_trie