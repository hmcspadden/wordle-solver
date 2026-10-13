import sys
import os

def read_text(filepath: str) -> list[str]:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")
    if not os.

    with open(filepath, "r") as f:


def build_trie(text: str) -> dict[str : str]:
    new_trie = {}



                