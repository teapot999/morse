MorseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-..', 'G': '--.',
             'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..'}


def encode_to_morse(text: str):
    t = list(text.upper())
    for i in range(len(t)):
        if t[i] in MorseCode:
            t[i] = MorseCode[t[i]]
    return ''.join(t)


print(encode_to_morse('te st'))  # => -. ...-
