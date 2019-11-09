# Name:  keyword_substitution.py
# Updated:  20191004

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
keywords = [
    "keyword", "Sophia", "Emily", "Hawkins", "guitar", "python",
    "hybrid",
]


def get_keyword():
    keyword = input("Enter keyword:  ").lower()
    for letter in keyword:
        if letter not in alphabet:
            keyword = keyword.replace(letter, "")
    return keyword


def set_keyword_shift(keyword):
    shifted_alphabet = ""
    for char in keyword:
        if char in alphabet:
            if not char in shifted_alphabet:
                shifted_alphabet += char

    for letter in alphabet:
        if not letter in shifted_alphabet:
            shifted_alphabet += letter
    return shifted_alphabet


def encrypt_keyword_sub(plaintext):
    ciphertext = ""
    shifted_alphabet = set_keyword_shift(get_keyword())
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += shifted_alphabet[index]
        else:
            ciphertext += char
    return ciphertext


def decrypt_keyword_sub(plaintext):
    pass


def get_random_alphabet(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ("".join(alphabet))
