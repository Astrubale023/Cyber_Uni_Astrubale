from collections import Counter

def getFreq(text):  #Gets the frequecies of every character given a string
    text = text.replace(" ", "") # Removes all the spaces
    return Counter(text)

with open("challenge.txt", "r") as file:
    cipher = ''.join(file.readlines())

conta = getFreq(cipher)
print(conta)

freq = {'L': 65, 'S': 52, 'P': 43, 'H': 40, 'E': 39, 'O': 33, 'A': 29, 'X': 26, 'D': 26, 'Y': 21,
        'U': 16, 'R': 15, 'W': 13, 'C': 11, 'V': 11, 'M': 11, 'K': 9, 'N': 9, ',': 8, '\n': 8, '.': 6,
        'Q': 5, 'Z': 5, '!': 5, '_': 5, ':': 4, 'F': 4, 'T': 2, 'B': 1, '?': 1, "'": 1, 'G': 1, '{': 1, '}': 1}