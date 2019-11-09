# Name:  shift_substition.py
# Updated:  20191004

alphabet = 'abcdefghijklmnopqrstuvwxyz'
reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'


def convert_rot13(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            ciphertext += alphabet[(alphabet.index(char) + 13) %
                                   (len(alphabet))]
        else:
            ciphertext += char
    return ciphertext


def encrypt_caesar(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            ciphertext += alphabet[(alphabet.index(char) + 3) %
                                   (len(alphabet))]
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char in alphabet.lower():
            plaintext += alphabet[(alphabet.index(char) - 3) % (len(alphabet))]
        else:
            plaintext += char
    return plaintext


def get_shift():
    key_shift = int(input("Enter key(#):  "))
    return key_shift


def encrypt_shift_substitution(plaintext):
    ciphertext = ""

    key = int(input("Enter the key (#):  "))
    for char in plaintext:
        if char in alphabet:
            ciphertext += alphabet[(alphabet.index(char) + key) %
                                   (len(alphabet))]
        else:
            ciphertext += char
    return ciphertext


def decrypt_shift_substitution(ciphertext):
    plaintext = ""

    key = int(input("Enter the key (#):  "))
    for char in ciphertext:
        if char in alphabet.lower():
            plaintext += alphabet[(alphabet.index(char) - key) %
                                  (len(alphabet))]
        else:
            plaintext += char
    return plaintext
