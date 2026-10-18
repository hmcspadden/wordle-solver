import os

#reads text from a filepath
def read_text(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise Exception("Filepath not found")

    with open(filepath, "r") as f:
        text = f.read()

    return text

#builds list of words from filepath
def build_word_list(filepath: str) -> list[str]:
    words = read_text(filepath)
    return words.split("\n")

#counts frequency of characters across all valid answers
def char_frequency(words: list[str]) -> dict[str, int]:
    frequency = {}

    for word in words:
        for char in word:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1

    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    return frequency

#builds matrix of characters ranked by positional frequency
def positional_char_frequency(words: list[str]) -> list[list[str]]:
    positional_frequency = {}
    
    #creates dictionary of positional char frequency
    for word in words:
        for i in range(len(word)):
            if word[i] not in positional_frequency:
                positional_frequency[word[i]] = [0,0,0,0,0]
            positional_frequency[word[i]][i] += 1
    
    matrix = []

    #converts dictionary into matrix
    for i in range(5):
        positional_values = []
        for char in positional_frequency:
            positional_values.append([char, positional_frequency[char][i]])
        
        positional_values = sorted(positional_values, key=lambda x: x[1], reverse=True)
        column = []
        for ch_val in positional_values:
            column.append(ch_val[0])
        
        matrix.append(column)

    return matrix

