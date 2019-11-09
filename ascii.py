# Name:  ascii.py
# Updated:  20190910


def convert_to_ascii(plaintext):
    plaintext = input('Enter your message:  ')
    ciphertext = ""
    for character in plaintext:
        ciphertext += str(ord(character))
        ciphertext += " "
    return ciphertext
