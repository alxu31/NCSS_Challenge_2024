
def decipher(msg) -> str:
    CODES = {
    'A': 'Y',
    'B': 'P',
    'C': 'W',
    'D': 'X',
    'E': 'U',
    'F': 'S',
    'G': 'T',
    'H': 'Z',
    'I': 'O',
    'J': 'R',
    'K': 'Q',
    'L': 'V',
    'M': 'N',
    'N': 'M',
    'O': 'I',
    'P': 'B',
    'Q': 'K',
    'R': 'J',
    'S': 'F',
    'T': 'G',
    'U': 'E',
    'V': 'L',
    'W': 'C',
    'X': 'D',
    'Y': 'A',
    'Z': 'H',
    ' ': ' ',
    }
    deciphered = []
    for letter in msg:
        letter = letter.upper()
        deciphered.append(CODES[letter])
    return "".join(deciphered)



msg = input("Message: ")

decipheredMsg = decipher(msg)
print(decipheredMsg)
