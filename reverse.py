# Name:  reverse.py
# Updated:  20190910


def reverse_cipher(plaintext):
    ciphertext = plaintext[::-1]
    return ciphertext


def reverse_cipher2(plaintext):
    ciphertext = ""
    i = len(plaintext) - 1
    while i >= 0:
        ciphertext += plaintext[i]
        i -= 1
    return ciphertext
