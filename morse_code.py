# Name:  morse_code.py
# Updated:  20190910

alphabet = 'abcdefghijklmnopqrstuvwxyz'
reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'

morse_code = {}


def encrypt_morse_code(plaintext):
    ciphertext = " ".join(plaintext)

    # morse code punctuation
    ciphertext = ciphertext.replace("-", "")
    ciphertext = ciphertext.replace(",", "")
    ciphertext = ciphertext.replace("'", "")
    ciphertext = ciphertext.replace('"', "")
    ciphertext = ciphertext.replace("*", "")
    ciphertext = ciphertext.replace(".", ".-.-.-")
    ciphertext = ciphertext.replace("?", "..--..")

    # morse code numbers
    ciphertext = ciphertext.replace("1", ".----")
    ciphertext = ciphertext.replace("2", "..---")
    ciphertext = ciphertext.replace("3", "...--")
    ciphertext = ciphertext.replace("4", "....-")
    ciphertext = ciphertext.replace("5", ".....")
    ciphertext = ciphertext.replace("6", "-....")
    ciphertext = ciphertext.replace("7", "--...")
    ciphertext = ciphertext.replace("8", "---..")
    ciphertext = ciphertext.replace("9", "----.")
    ciphertext = ciphertext.replace("0", "-----")

    # morse code letters
    ciphertext = ciphertext.replace("a", ".-")
    ciphertext = ciphertext.replace("b", "-...")
    ciphertext = ciphertext.replace("c", "-.-.")
    ciphertext = ciphertext.replace("d", "-..")
    ciphertext = ciphertext.replace("e", ".")
    ciphertext = ciphertext.replace("f", "..-.")
    ciphertext = ciphertext.replace("g", "--.")
    ciphertext = ciphertext.replace("h", "....")
    ciphertext = ciphertext.replace("i", "..")
    ciphertext = ciphertext.replace("j", ".---")
    ciphertext = ciphertext.replace("k", "-.-")
    ciphertext = ciphertext.replace("l", ".-..")
    ciphertext = ciphertext.replace("m", "--")
    ciphertext = ciphertext.replace("n", "-.")
    ciphertext = ciphertext.replace("o", "---")
    ciphertext = ciphertext.replace("p", ".--.")
    ciphertext = ciphertext.replace("q", "--.-")
    ciphertext = ciphertext.replace("r", ".-.")
    ciphertext = ciphertext.replace("s", "...")
    ciphertext = ciphertext.replace("t", "-")
    ciphertext = ciphertext.replace("u", "..-")
    ciphertext = ciphertext.replace("v", "...-")
    ciphertext = ciphertext.replace("w", ".--")
    ciphertext = ciphertext.replace("x", "-..-")
    ciphertext = ciphertext.replace("y", "-.--")
    ciphertext = ciphertext.replace("z", "--..")

    return ciphertext


def decrypt_morse_code(ciphertext):
    pass


def summarize_morse_code():
    pass
