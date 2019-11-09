# Vigenere Cipher
# vigenere.py
# Updated:  20191006

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encode_vigenere():
    ciphertext = ""
    keyword = "tasty"
    plaintext = "I like macaroni and cheese!"
    i = 0
    for char in plaintext.lower():
        if i == len(keyword):
            i = 0
        if char in alphabet:
            ciphertext += alphabet[(alphabet.index(char) + alphabet.index(
                keyword[i])) % len(alphabet)]
            i += 1

    return ciphertext


print(encode_vigenere())
