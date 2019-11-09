# freqency_analysis.py
# Created:  20190912
# Updated:  20190912


def analyze_frequency(ciphertext):
    stored_letters = {}
    for char in ciphertext:
        if char not in ['.', ',', '!', '?', ' ', "'"]:
            if not char in stored_letters:
                stored_letters[char] = 1
            else:
                stored_letters[char] += 1

    print(ciphertext)
    print()
    for key, value in sorted(stored_letters.items()):
        print(key + ": ", value)

    return stored_letters


ciphertext = " "
analyze_frequency(ciphertext)
